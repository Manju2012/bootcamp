from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-ccbc479441ad.json" # storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-569673e95ac5.json" # bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.

# 1. customer_master
job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV,
    skip_leading_rows = 1,
    schema = [
            bigquery.SchemaField("customerid", "INTEGER"),
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("address", "STRING"),
            bigquery.SchemaField("city", "STRING"),
            bigquery.SchemaField("state", "STRING"),
            bigquery.SchemaField("pincode", "INTEGER")
            ]
    )
table_name = 'customer_master'


# # 2. product_master
# job_config = bigquery.LoadJobConfig(
#     source_format = bigquery.SourceFormat.CSV,
#     skip_leading_rows = 1,
#     schema = [
#             bigquery.SchemaField("productid", "INTEGER"),
#             bigquery.SchemaField("productcode", "STRING"),
#             bigquery.SchemaField("productname", "STRING"),
#             bigquery.SchemaField("sku", "STRING"),
#             bigquery.SchemaField("rate", "INTEGER"),
#             bigquery.SchemaField("isactive", "BOOLEAN")
#             ]
#     )
# table_name = 'product_master'


# # 3. order_details
# job_config = bigquery.LoadJobConfig(
#     source_format = bigquery.SourceFormat.CSV,
#     skip_leading_rows = 1,
#     schema = [
#             bigquery.SchemaField("orderid", "INTEGER"),
#             bigquery.SchemaField("customerid", "INTEGER"),
#             bigquery.SchemaField("orderplaceddatetime", "DATETIME"),
#             bigquery.SchemaField("ordercompletiondatetime", "DATETIME"),
#             bigquery.SchemaField("orderstatus", "STRING")
#             ]
#     )
# table_name = 'order_details'


# # 4. order_quantity
# job_config = bigquery.LoadJobConfig(
#     source_format = bigquery.SourceFormat.CSV,
#     skip_leading_rows = 1,
#     schema = [
#             bigquery.SchemaField("orderid", "INTEGER"),
#             bigquery.SchemaField("productid", "INTEGER"),
#             bigquery.SchemaField("quantity", "INTEGER"),
#             ]
#     )
# table_name = 'order_quantity'



project_id = 'btcmp-1'
dataset_id = 'mydukan'
table_id = f"{project_id}.{dataset_id}.{table_name}"


uri = f"gs://btcmp-bucket1/{table_name}.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)

print("Loaded {} rows to table {}".format(table.num_rows, table_id))