FROM python:3.8-slim-bullseye

# Install basic tools and clean up
RUN apt update -y && apt install -y groff less && apt clean

# Install AWS CLI using pip (much more stable)
RUN pip install --upgrade pip
RUN pip install awscli

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]