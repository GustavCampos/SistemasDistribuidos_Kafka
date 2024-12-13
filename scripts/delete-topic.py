from sys import argv
from confluent_kafka.admin import AdminClient
from config import KAFKA_CONF as conf


admin_client = AdminClient(conf=conf)

topics_to_delete = [arg for arg in argv[1:]]

request = admin_client.delete_topics(topics_to_delete)

for topic, req in request.items():
    try:
        req.result()
        print(f"Topic '{topic}' deleted successfully!")
        
    except Exception as e:
        print(f"Failed on delete topic '{topic}': {e}")