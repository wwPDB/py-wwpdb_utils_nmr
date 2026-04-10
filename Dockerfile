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

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies for resource update
RUN pip install \
        --no-cache-dir \
        -r standalone_update_requirements.txt

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Run ChemCompUpdater.py
# This creates: wwpdb/utils/nmr/ligand_dict
RUN python wwpdb/utils/nmr/ChemCompUpdater.py

# Run BMRBCsStatUpdater.py
# This updates: wwpdb/utils/nmr/bmrb_cs_stat
RUN python wwpdb/utils/nmr/BmrbCsStatUpdater.py

# Install Python dependencies for runtime
RUN CFLAGS="-Wno-implicit-function-declaration -Wno-int-conversion" pip install \
        --no-cache-dir \
        --prefix=/install \
        -r standalone_runtime_requirements.txt

# Remove micellaneous files to reduce image size
RUN rm -f .dockerignore \
          Dockerfile \
          *.txt \
          wwpdb/utils/nmr/components.cif.gz \
          wwpdb/utils/nmr/bmrb_cs_stat/*.csv \
          wwpdb/utils/nmr/ChemCompUpdater.py \
          wwpdb/utils/nmr/BmrbCsStatUpdater.py

# ============================================================
# Stage 2: Runtime (minimal, non-root)
# ============================================================
FROM python:3.12-alpine

# Runtime OS deps
RUN apk add --no-cache ca-certificates

# Create non-root user
RUN addgroup -S appuser && \
    adduser -S appuser -G appuser -D

# Copy installed Python environment
COPY --from=builder /install /usr/local

# Copy application code with generated ligand_dict
COPY --from=builder --chown=appuser:appuser /opt/py-wwpdb_utils_nmr /opt/py-wwpdb_utils_nmr

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Set working directory
WORKDIR /mnt

# Switch to no-root user
USER appuser

# Default command
CMD ["python"]
