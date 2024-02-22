FROM python:3.10-slim

LABEL maintainer="learnaimee@gmail.com"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set TRANSFORMERS_CACHE environment variable
ENV HF_HOME="/app/analysys"

# Copy requirements files and application code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Set working directory
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Set a build argument for development environment
ARG DEV=false

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /py \
    && /py/bin/pip install --upgrade pip \
    # && /py/bin/python -m pip install "psycopg2[binary]" \
    && /py/bin/pip install -r /tmp/requirements.txt \
    && if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi \
    && rm -rf /tmp \
    && adduser \
        --disabled-password \
        --no-create-home \
        django-user \
    && mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol \
    && chown -R django-user:django-user /app/analysys \
    && chmod -R 777 /app/analysys 

# Set PATH environment variable
ENV PATH="/py/bin:${PATH}"

# Switch to non-root user
USER django-user
