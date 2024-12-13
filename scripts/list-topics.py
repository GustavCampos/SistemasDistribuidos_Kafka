from confluent_kafka.admin import AdminClient
from config import KAFKA_CONF as conf


admin_client = AdminClient(conf=conf)

try:
    metadata = admin_client.list_topics(timeout=10)

    for topic in metadata.topics.keys():
        print(f"- {topic}")

except Exception as e:
    print(f"Something unexpected happened: {e}")