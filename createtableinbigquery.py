from google.cloud import bigquery

client = bigquery.Client()

# Set this as your project, the dataset, and the table name you wish to create
table_id = "project_name.dataset_name.table_name"

# Creating a config for the job, to  be including in the API call
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
    ],
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Overwrites the table (defaults to WRITE_APPEND)
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,  # Source format, default is CSV
)

uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"  # Cloud Storage URI

load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)

load_job.result()

destination_table = client.get_table(table_id)
print(f"Loaded {destination_table.num_rows} rows.")
