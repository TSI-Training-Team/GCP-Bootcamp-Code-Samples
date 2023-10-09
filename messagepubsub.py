from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('gcptests-399609', 'mytopic')

data_str = f"hello world!"
# Data must be a bytestring
data = data_str.encode("utf-8")
# Add two attributes, origin and username, to the message
future = publisher.publish(
    topic_path, data, origin="python-sample", username="gcp"
)

print(future.result())

print(f"Published!")
