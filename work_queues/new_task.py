import pika

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

with pika.BlockingConnection(params) as connection:
    with connection.channel() as channel:
        channel.queue_declare(queue='task_queue', durable=True)
        for i in range(10):
            channel.basic_publish(exchange='',
                                  routing_key='task_queue',
                                  body=f'Hello World - {i}',
                                  properties=pika.BasicProperties(
                                      delivery_mode=pika.DeliveryMode.Persistent)) # сохраняет сообщения после перезагрузки сервиса