# ============================================================
# Stage 1: Builder
# ============================================================
FROM python:3.12-slim AS builder

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Ignore irrelevant warning of pip
ENV PIP_ROOT_USER_ACTION=ignore

# Minimal build deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy the repository
COPY . /opt/py-wwpdb_utils_nmr

# Move working directory to the repo directory
WORKDIR /opt/py-wwpdb_utils_nmr

# System version information holder file under the current working directory
ENV VER_INFO=.ver_info

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies for resource update
RUN pip install \
        --no-cache-dir \
        -r standalone_update_requirements.txt

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Extract package version information -> UTILS_NMR_VER
RUN grep version wwpdb/utils/nmr/__init__.py \
    | sed -e 's/__version__ = /export UTILS_NMR_VER=/' \
    | sed -e 's/"//g' > ${VER_INFO}

# Run ChemCompUpdater.py
# This creates: wwpdb/utils/nmr/ligand_dict
# Release date of Chemical Component Dictionary (CCD) -> CCD_REL
RUN CCD_REL_DATE_FILE=wwpdb/utils/nmr/ligand_dict/.ccd_rel_date \
    && python wwpdb/utils/nmr/ChemCompUpdater.py \
    && CCD_REL=`cat ${CCD_REL_DATE_FILE}` \
    && rm -f ${CCD_REL_DATE_FILE} \
    && echo "export CCD_REL=${CCD_REL}" >> ${VER_INFO}

# Run BMRBCsStatUpdater.py
# This updates: wwpdb/utils/nmr/bmrb_cs_stat
# Release date of BMRB chemical shift statistics -> CS_STAT_REL
RUN CS_STAT_REL_DATE_FILE=wwpdb/utils/nmr/bmrb_cs_stat/.cs_stat_rel_date \
    && python wwpdb/utils/nmr/BmrbCsStatUpdater.py \
    && CS_STAT_REL=`cat ${CS_STAT_REL_DATE_FILE}` \
    && rm -f ${CS_STAT_REL_DATE_FILE} \
    && echo "export CS_STAT_REL=${CS_STAT_REL}" >> ${VER_INFO}

# Install Python dependencies for runtime
RUN CFLAGS="-Wno-implicit-function-declaration -Wno-int-conversion" pip install \
        --no-cache-dir \
        --target=/install \
        -r standalone_runtime_requirements.txt

# Remove micellaneous files to reduce image size
RUN rm -f .dockerignore \
          Dockerfile \
          *.txt \
          wwpdb/utils/nmr/components.cif.gz \
          wwpdb/utils/nmr/ChemCompUpdater.py \
          wwpdb/utils/nmr/BmrbCsStatUpdater.py

# ============================================================
# Stage 2: Runtime (minimal, non-root)
# ============================================================
FROM python:3.12-slim

# Runtime OS deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 appuser

# Copy installed Python environment
COPY --from=builder /install /opt/py-packages

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-packages:/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Copy application code with generated ligand_dict
COPY --from=builder --chown=appuser:appuser /opt/py-wwpdb_utils_nmr /opt/py-wwpdb_utils_nmr

# System version information holder file
ENV VER_INFO=/opt/py-wwpdb_utils_nmr/.ver_info

# Create entrypoint script executable with exporting version information
RUN echo "#!/bin/sh" > /opt/entrypoint.sh && \
    echo "set -e" >> /opt/entrypoint.sh && \
    cat ${VER_INFO} >> /opt/entrypoint.sh && \
    echo 'exec "$@"' >> /opt/entrypoint.sh && \
    chmod +x /opt/entrypoint.sh && \
    rm -f ${VER_INFO}

# Set working directory
WORKDIR /mnt

# Switch to no-root user
USER appuser

# Set the entrypoint
ENTRYPOINT ["/opt/entrypoint.sh"]
