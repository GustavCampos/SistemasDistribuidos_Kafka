from sys import argv
from confluent_kafka import Consumer
from config import KAFKA_CONSUMER_CONF as conf


consumer = Consumer(conf)

topic = argv[1]
consumer.subscribe([topic])

print(f"Consuming from topic '{topic}'. Press Ctrl+C to stop.")

try:
    while True:
        msg = consumer.poll(1)
        
        if msg is None: continue
        
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"> {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()