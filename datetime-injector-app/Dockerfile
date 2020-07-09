FROM python:3.7.8-slim-stretch

RUN pip install flask confluent-kafka

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]