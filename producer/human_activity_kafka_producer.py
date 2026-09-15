import json
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

count = 0

# Read JSON file line by line
with open("data/human_activity.json", "r") as file:

    for line in file:
        if line.strip():

            activity = json.loads(line)

            # Send event to Kafka
            producer.send("human-activity", value=activity)

            count += 1

# Make sure all events are sent
producer.flush()

print(f"Sent {count} events to Kafka.")