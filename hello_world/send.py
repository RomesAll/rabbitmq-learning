from pika import URLParameters
import pika

url = URLParameters(url='amqp://guest:guest@127.0.0.1:5672/')

with pika.BlockingConnection(parameters=url) as connection:
    with connection.channel() as channel:
        channel.queue_declare(queue='hello') # добавить очередь
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!') # отправить сообщение