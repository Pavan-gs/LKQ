# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy app, model, templates, and static files
COPY app.py churn_model.pkl requirements.txt /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port for Flask app
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]