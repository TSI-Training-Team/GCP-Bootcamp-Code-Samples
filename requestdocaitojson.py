import base64
import functions_framework
from datetime import datetime
from google.cloud import aiplatform
from google.cloud import storage
import json

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    print(cloud_event.data["message"]["data"])

    aiplatform.init(project="250193706", location="europe-central2")

    endpoint = aiplatform.Endpoint("6336793374128865280")

    prediction = endpoint.predict(instances=[{
    "sepal_length": 5.1, "sepal_width": 3.5,
    "petal_length": 1.4, "petal_width": 0.2
    }])
    print(prediction.predictions)

    client2 = storage.Client()

    bucket = client2.get_bucket('testbucketliamw')

    with open("test.json", "w") as outfile:
      json.dump(prediction.predictions[0], outfile)

    blob = bucket.blob('test.json')
    blob.upload_from_filename('test.json')