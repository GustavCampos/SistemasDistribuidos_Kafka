KAFKA_ENDPOINT = "localhost"

KAFKA_CONF = {
    'bootstrap.servers': f'{KAFKA_ENDPOINT}:29092,{KAFKA_ENDPOINT}:39092,{KAFKA_ENDPOINT}:49092'  # Adjust to match your setup
}

KAFKA_CONSUMER_CONF = {
    **KAFKA_CONF,
    'group.id': 'consumer-group',  # Unique group id for the consumer
    'auto.offset.reset': 'earliest',  # Start reading at the beginning if no offset exists
}