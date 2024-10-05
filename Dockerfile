# Starting with a small Python image
FROM python:3.10-slim

# Setting working directory inside the container
WORKDIR /app

# Copying requirements first to leverage Docker cache
COPY requirements.txt /app/

# Installing required system packages and Python dependencies
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# We hav an Image Folder so,to get Images..
COPY ./images /app/images

# Exposing port 8501 for Streamlit
EXPOSE 8501

# Running our Streamlit app when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
