FROM python:3.11.1-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app/code
COPY ./app /app/code

ENTRYPOINT ["bash", "/app/docker-entrypoint.sh"]