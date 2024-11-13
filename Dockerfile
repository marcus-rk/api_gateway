FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose port 80
EXPOSE 5001

# Run with gunicorn on port 80
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app", "--access-logfile", "-"]