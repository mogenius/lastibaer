# Use a base image with Python installed
FROM python:3.9-slim

# Set environment variables
ENV TRAFFIC_RATE=100
ENV CPU_LOAD=50
ENV RAM_LOAD=500
ENV INTERVAL_MINUTES=1
ENV DOWNLOAD_SIZE_LIMIT=2m

# Install required packages
RUN apt-get update && apt-get install -y stress-ng wget

# Copy the workload generator script into the container
COPY workload_generator.py /usr/src/app/workload_generator.py

# Set the working directory
WORKDIR /usr/src/app

# Run the workload generator script
CMD ["python", "workload_generator.py"]
