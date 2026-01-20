from pika import URLParameters
import pika

url = URLParameters(url='amqp://guest:guest@127.0.0.1:5672/')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

with pika.BlockingConnection(parameters=url) as connection:
    with connection.channel() as channel:
        channel.queue_declare(queue='hello')
        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True) # указать какую очередь слушаем и как обрабатываем
        channel.start_consuming() # начать слушать