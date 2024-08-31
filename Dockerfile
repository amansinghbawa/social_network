# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Copy the wait script into the container
# COPY wait_for_it.sh /app/

# Ensure the wait script is executable
# RUN chmod +x /app/wait_for_it.sh

# Expose the port the app runs on
EXPOSE 8000
EXPOSE 5432

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=social_network.settings
ENV PYTHONUNBUFFERED=1

# Run database migrations and start the server
# CMD ["sh", "-c", "/app/wait_for_it.sh db 'python manage.py migrate && python manage.py runserver 0.0.0.0:8000'"]
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
