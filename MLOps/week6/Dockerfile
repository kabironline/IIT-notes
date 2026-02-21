# Use a slim Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies using pip, without caching, into the system environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and the trained model
COPY ./main.py .
COPY ./models ./models

# Expose the port the app runs on
EXPOSE 8000

# Command to run the uvicorn server
# --host 0.0.0.0 makes the server accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
