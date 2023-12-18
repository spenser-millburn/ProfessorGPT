# Base image
FROM python:3.9

# Install dependencies
RUN pip3 install --no-cache-dir  openai fastapi uvicorn

# Set working directory
WORKDIR /app

# Copy necessary files
COPY . /app/

# Command to run the application
CMD ["python3", "api.py"]
