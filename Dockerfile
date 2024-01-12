# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy only manage.py into the container at /app
COPY manage.py .

# Copy the rest of the current directory contents into the container at /app
COPY . .

# Debugging: List files in the current directory
RUN ls -l

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

