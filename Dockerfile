# Use Python slim image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3-dev musl-dev \
    build-essential \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies (make sure Celery is in your requirements.txt)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .
RUN python manage.py collectstatic --noinput
# Expose ports for Gunicorn and Cassandra
EXPOSE 8000
# Set Gunicorn as the default command
CMD ["sh", "-c", "gunicorn market.wsgi:application --workers 4 --bind 0.0.0.0:8000"]

