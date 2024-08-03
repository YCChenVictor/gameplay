# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Run main.py when the container launches
CMD ["python", "main.py"]
