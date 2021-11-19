from google.cloud import bigquery
from oauth2client.service_account import ServiceAccountCredentials
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-ccbc479441ad.json" # storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-569673e95ac5.json" # bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "btcmp-1.btcmp_step4.netflix1"

job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV,
    skip_leading_rows = 1,
    # expiration_ms = 2592000000,  # 90 days.
    schema = [
            bigquery.SchemaField("Title", "STRING"),
            bigquery.SchemaField("Genre", "STRING"),
            bigquery.SchemaField("Tags", "STRING"),
            bigquery.SchemaField("Languages", "STRING"),
            bigquery.SchemaField("Series_or_Movie", "STRING"),
            bigquery.SchemaField("Hidden_Gem_Score", "FLOAT"),
            bigquery.SchemaField("Country_Availability", "STRING"),
            bigquery.SchemaField("Runtime", "STRING"),
            bigquery.SchemaField("Director", "STRING"),
            bigquery.SchemaField("Writer", "STRING"),
            bigquery.SchemaField("Actors", "STRING"),
            bigquery.SchemaField("View_Rating", "STRING"),
            bigquery.SchemaField("IMDB_Score", "FLOAT"),
            bigquery.SchemaField("Rotten_Tomatoes_Score", "FLOAT"),
            bigquery.SchemaField("MetaCritic_Score", "FLOAT"),
            bigquery.SchemaField("Awards_Received", "FLOAT"),
            bigquery.SchemaField("Awards_Nominated_For", "FLOAT"),
            bigquery.SchemaField("Boxoffice", "INTEGER"),
            bigquery.SchemaField("Release_Date", "DATE"),
            bigquery.SchemaField("Netflix_Release_Date", "DATE"),
            bigquery.SchemaField("Production_House", "STRING"),
            bigquery.SchemaField("Netflix_Link", "STRING"),
            bigquery.SchemaField("IMDb_Link", "STRING"),
            bigquery.SchemaField("Summary", "STRING"),
            bigquery.SchemaField("IMDb_Votes", "FLOAT"),
            bigquery.SchemaField("Image", "STRING"),
            bigquery.SchemaField("Poster", "STRING"),
            bigquery.SchemaField("TMDb_Trailer", "STRING"),
            bigquery.SchemaField("Trailer_Site", "STRING")
            ]
    )

uri = "gs://btcmp-bucket/netflix1.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)

print("Loaded {} rows to table {}".format(table.num_rows, table_id))