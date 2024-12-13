from sys import argv
from confluent_kafka.admin import AdminClient, NewTopic
from config import KAFKA_CONF as conf


admin_client = AdminClient(conf=conf)

topics = [NewTopic(arg, num_partitions=3, replication_factor=3) for arg in argv[1:]]

request = admin_client.create_topics(topics)

for topic, req in request.items():
    try:
        req.result()
        print(f"Topic {topic} created successfully!")
    
    except Exception as e:
        print(f"Failed to create topic '{topic}': {e}")
