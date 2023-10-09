from google.cloud import bigquery

client = bigquery.Client()

# Simple GoogleSQL can be replaced with your own
query_job = client.query(
    """
    SELECT *
    FROM `project_name.dataset_name.table_name`
    LIMIT 10
    """
)

results = query_job.result()  # Waits for job completion and returns the result

for row in results:
    print(f"{row.name} : {row.post_abbr}")
