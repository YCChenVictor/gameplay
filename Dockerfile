# Use the official Python image from the Docker Hub
FROM python:3.9-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends xvfb
RUN apt-get install -y --no-install-recommends xauth
RUN apt-get install -y --no-install-recommends python3-tk python3-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
WORKDIR /app

CMD ["sh", "-c", "xvfb-run -s '-screen 0 1024x768x24' -- python main.py"]
