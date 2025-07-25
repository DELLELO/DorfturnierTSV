FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Create migrations and migrate
RUN python manage.py makemigrations || true
RUN python manage.py migrate || true

EXPOSE 8000

# Use environment variable for port, fallback to 8000
CMD python manage.py runserver 0.0.0.0:${PORT:-8000}