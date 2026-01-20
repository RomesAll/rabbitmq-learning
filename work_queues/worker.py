import time
import pika
from pika.channel import Channel

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

def callback(ch: Channel, method, properties, body: bytes):
    try:
        print(" [x] Received %r" % body)
        time.sleep(5)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except:
        ch.basic_nack(delivery_tag=method.delivery_tag)

with pika.BlockingConnection(params) as connection:
    with connection.channel() as channel:
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_consume(queue='task_queue',
                              on_message_callback=callback,
                              auto_ack=False)
        channel.basic_qos(prefetch_count=1) # кол-во сообщений за раз
        channel.start_consuming()