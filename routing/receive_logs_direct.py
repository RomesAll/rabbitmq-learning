import pika

params = pika.URLParameters(url='amqp://guest:guest@localhost:5672/')

with pika.BlockingConnection(parameters=params) as connection:
    with connection.channel() as channel:
        channel.exchange_declare('direct_logs', exchange_type='direct')
        queue1 = channel.queue_declare(queue='', exclusive=True)
        queue2 = channel.queue_declare(queue='', exclusive=True)

        channel.queue_bind(exchange='direct_logs', queue=queue1.method.queue, routing_key='exc')
        channel.queue_bind(exchange='direct_logs', queue=queue2.method.queue, routing_key='error')

        def callback(ch, method, properties, body):
            print(f" [x] {method.routing_key}:{body}")

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue=queue1.method.queue, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()