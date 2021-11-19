import os
import pandas as pd
from google.cloud import bigquery

path = "/home/fagcpdebc1_09/test/btcmp-1-569673e95ac5.json"   #bigquery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= path

client = bigquery.Client() # Start the BigQuery Client
QUERY = 'select * from bigquery-public-data.austin_bikeshare.bikeshare_trips limit 100'
query_job = client.query(QUERY) # Start Query API Request
query_result = query_job.result() # Get Query Result
df = query_result.to_dataframe() # Save the Query Resultto Dataframe

print(df)