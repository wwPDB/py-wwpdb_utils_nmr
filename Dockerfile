# ============================================================
# Stage 1: Builder
# ============================================================
# Use a slim but full-featured Python base image
FROM python:3.11-slim AS builder

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /opt

# Minimal build deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git build-essential \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Clone the py-wwpdb_utils_nmr repository
RUN git clone https://github.com/yokochi47/py-wwpdb_utils_nmr.git

WORKDIR /opt/py-wwpdb_utils_nmr

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies for resource update
RUN CFLAGS="-Wno-implicit-function-declaration -Wno-int-conversion" pip install \
        --no-cache-dir \
        -r bmrb-extract_requirements.txt

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Run ChemCompUpdater.py
# This creates: wwpdb/utils/nmr/ligand_dict
RUN python wwpdb/utils/nmr/ChemCompUpdater.py

# Run BMRBCsStatUpdater.py
# This updates: wwpdb/utils/nmr/bmrb_cs_stat
RUN python wwpdb/utils/nmr/BMRBCsStatUpdater.py

# Remove .git, unit test directories and micellaneous files to reduce image size
RUN rm -rf .git\
           wwpdb/utils/tests-nmr \
           wwpdb/utils/tests-nmr-tox\
           wwpdb/utils/nmr/nef/lib \
           wwpdb/utils/nmr/ann/lib && \
    rm -f .gitignore .gitlab-ci.yml Dockerfile MANIFEST.in *.yml pylintc setup.* tox.ini && \
    cat bmrb-extract_requirements.txt | grep -v python-dateutil | grep -v requests > bmrb-extract_min_requirements.txt && \
    rm -f wwpdb/utils/nmr/components.cif.gz wwpdb/utils/nmr/ChemCompUpdater.py wwpdb/utils/nmr/BMRBCsStatUpdater.py

# Install Python dependencies for runtime
RUN CFLAGS="-Wno-implicit-function-declaration -Wno-int-conversion" pip install \
        --no-cache-dir \
        --prefix=/install \
        -r bmrb-extract_min_requirements.txt

# Remove requirement.txt
RUN rm -f *.txt

# ============================================================
# Stage 2: Runtime (minimal, non-root)
# ============================================================
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Minimal build deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r webmaster && useradd -r -g webmaster -s /bin/bash webmaster

# Copy installed Python environment
COPY --from=builder /install /usr/local

# Copy application code with generated ligand_dict
COPY --from=builder --chown=webmaster:webmaster /opt/py-wwpdb_utils_nmr /opt/py-wwpdb_utils_nmr

# Working directory
WORKDIR /opt/py-wwpdb_utils_nmr

# Switch to no-root use
USER webmaster

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Default command
CMD ["python"]
