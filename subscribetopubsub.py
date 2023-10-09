from google.cloud import pubsub_v1


# Callback function that is called when a message is received!
def callback(message):
    print(f"Received {message}.")
    # Acknowledge the message. They will be resent otherwise.
    message.ack()
    print(f"Acknowledged {message.message_id}.")


# Receives messages from a Pub/Sub subscription.
subscriber_client = pubsub_v1.SubscriberClient()
# Setting the path to the subscription, not the topic!
subscription_path = subscriber_client.subscription_path('gcptests-399609', 'easyname')

# Subscribes to the subscription created in Pub/Sub and sets a callback to be called when a message is received
streaming_pull_future = subscriber_client.subscribe(
    subscription_path, callback=callback
)

# Convenient console message
print(f"Listening for messages on {subscription_path}\n")

try:
    # Tries pulling messages, waits for 600 seconds
    streaming_pull_future.result(timeout=600)
except:  # noqa
    streaming_pull_future.cancel()
    streaming_pull_future.result()

# Closes the subscription
subscriber_client.close()
