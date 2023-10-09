# pip install google-cloud-bigquery
from google.cloud import bigquery

client = bigquery.Client()

# FORMAT IS project_name.dataset_name, use your project name and make a dataset name
dataset_id = "yourproject.datasetname".format(client.project)

dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"  # You can use EU here if you wish

dataset = client.create_dataset(dataset, timeout=30)
print(f"Created dataset {client.project}.{dataset.dataset_id}")
