import pika

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

with pika.BlockingConnection(params) as connection:
    with connection.channel() as channel:
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body='Hello World',
                              properties=pika.BasicProperties(delivery_mode=2))