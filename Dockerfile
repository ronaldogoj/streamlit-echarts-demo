# Use the official Python Slim image as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8501
EXPOSE 8501

# Set the name of the image
LABEL maintainer="Ronaldo Geraidine <ronaldogoj@gmail.com>" \
      description="Rateio Conta Água Quintessenza" \
      version="1.0"

# Command to run the application
CMD ["streamlit", "run", "app-v2.py"]