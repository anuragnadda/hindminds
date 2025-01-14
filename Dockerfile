# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose port 8000 (the default port for Django)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
