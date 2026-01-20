import pika

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

with pika.BlockingConnection(params) as connection:
    with connection.channel() as channel:
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        queue = channel.queue_declare(queue='', exclusive=True) # очередь удалиться после отключания всех consumers
        channel.queue_bind(exchange='logs', queue=queue.method.queue)
        channel.basic_consume(queue=queue.method.queue, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()