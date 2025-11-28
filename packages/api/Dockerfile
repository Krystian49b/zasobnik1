FROM python:3.13-slim as builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy workspace files
COPY pyproject.toml uv.lock ./
COPY packages/common ./packages/common
COPY packages/api ./packages/api

# Install dependencies
RUN uv sync --package api --no-dev

# Runtime stage
FROM python:3.13-slim

WORKDIR /app

# Copy virtual environment and application
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/packages /app/packages

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
