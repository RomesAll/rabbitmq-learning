import pika

params = pika.URLParameters(url='amqp://guest:guest@localhost:5672/')

with pika.BlockingConnection(params) as connection:
    with connection.channel() as channel:
        channel.exchange_declare('direct_logs', exchange_type='direct')
        for _ in range(10):
            channel.basic_publish(exchange='direct_logs', routing_key='exc', body='Hello World')
            channel.basic_publish(exchange='direct_logs', routing_key='error', body='End world')