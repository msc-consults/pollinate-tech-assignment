FROM python

RUN pip install flask confluent-kafka

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]