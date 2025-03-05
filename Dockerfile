# Dockerfile
FROM python:3.10.11-slim

WORKDIR /app

# Copy all files into the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port your app uses (adjust as needed)
EXPOSE 8000

# Command to run your app (adjust the entry point as needed)
CMD ["uvicorn", "api/chat:app", "--host", "0.0.0.0", "--port", "8000"]
