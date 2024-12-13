from sys import argv
from confluent_kafka import Producer
from config import KAFKA_CONF as conf


def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


producer = Producer(conf)
        
topic = argv[1] # First custom arg

try:
    print(f"Writing on {topic}!")
    print("Use '!q' to exit")
    
    while True:
        message = input("> ")
        
        if message.lower() == "!q": break
        
        producer.produce(topic, message.encode("utf-8"), callback=delivery_report)
        producer.flush()
        
except KeyboardInterrupt:
    print("\nProducer stopped.")

finally:
    producer.flush()