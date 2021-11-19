
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

path = '/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-ccbc479441ad.json' #storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

client = storage.Client()
bucket = client.get_bucket('btcmp-bucket')
blob = bucket.blob('netflix2')

blob.upload_from_filename("/home/fagcpdebc1_09/netflix-rotten-tomatoes-metacritic-imdb.csv")
print(bucket)