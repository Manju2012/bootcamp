import psycopg2
import datetime
import os
from google.cloud import bigquery
import pandas as pd
import pandas_gbq
import pytz
import logging
import google.cloud.logging


def use_logging_handler():
	clientlogging = google.cloud.logging.Client()
	clientlogging.setup_logging()
	text = "DAtaframe Generated"
	logging.info(text)
	print("Logged: {}".format(text))

  
bq_path = "/home/fagcpdebc1_09/ServiceAccountKeys/BigQuery/btcmp-1-569673e95ac5.json"  
    # bq token path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= bq_path
	
    
def query(q):
	conn = psycopg2.connect(host="35.225.145.213",port="5432", database="myorg", user="postgres", password="Manju@2012")
	return pd.read_sql(q, conn)


project = 'btcmp-1'
client = bigquery.Client(project=project)
job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
dataset= 'pgdataset'



table=['project','employee','project_staff','department']
	# array for list of tables to be created and input data

schema = [
        [
            {'name':'proj_id', 'type': 'INT64'},
            {'name':'proj_name', 'type': 'STRING'},
            {'name':'dept_id', 'type': 'INT64'},
            {'name':'proj_start_date', 'type': 'DATE'},
            {'name':'proj_end_date', 'type': 'DATE'}
        ],
        [
            {'name':'emp_id', 'type':'INT64'},
            {'name':'proj_name', 'type': 'STRING'},
            {'name':'name', 'type':'STRING'},
            {'name':'dept_id', 'type':'INT64'},
            {'name':'salary', 'type':'INT64'},
            {'name':'joining_date', 'type':'DATE'},
            {'name':'leaving_date', 'type':'DATE'},
            {'name':'is_active', 'type':'BOOLEAN'}
        ],
        [
            {'name':'proj_id', 'type': 'INT64'},
            {'name':'emp_id', 'type': 'INT64'},
            {'name':'role_name', 'type': 'STRING'},
            {'name':'start_date', 'type': 'DATE'},
            {'name':'end_date', 'type': 'DATE'}
        ],
        [
            {'name':'dept_id', 'type': 'INT64'},
            {'name':'dept_name', 'type': 'STRING'},
            {'name':'dept_head_id', 'type': 'INT64'}
        ]
    ]


# for n,i in zip(table,[0,1,2,3]):
# print(n)

st='SELECT * FROM ' + 'project'
df = query (st)
#df2=pd.DataFrame(df)
#print(df2)
#print(df2.dtypes)
table_id="btcmp-1.{}.{}".format(dataset,'project_staff')
table = bigquery.Table(table_id)
job1 = pandas_gbq.to_gbq(df, table_id, table_schema=schema[0], if_exists="replace")
print("Loaded {}".format( table_id ))


st='SELECT * FROM ' + 'employee'
df = query (st)
#df2=pd.DataFrame(df)
#print(df2)
#print(df2.dtypes)
table_id="btcmp-1.{}.{}".format(dataset,'employee')
table = bigquery.Table(table_id)
job2 = pandas_gbq.to_gbq(df, table_id, table_schema=schema[1], if_exists="replace")
print("Loaded {}".format( table_id ))


st='SELECT * FROM ' + 'project_staff'
df = query (st)
#df2=pd.DataFrame(df)
#print(df2)
#print(df2.dtypes)
table_id="btcmp-1.{}.{}".format(dataset,'project_staff')
table = bigquery.Table(table_id)
job3 = pandas_gbq.to_gbq(df, table_id, table_schema=schema[2], if_exists="replace")
print("Loaded {}".format( table_id ))

st='SELECT * FROM ' + 'department'
df = query (st)
#df2=pd.DataFrame(df)
#print(df2)
#print(df2.dtypes)
table_id="btcmp-1.{}.{}".format(dataset,'department')
table = bigquery.Table(table_id)
job4 = pandas_gbq.to_gbq(df, table_id, table_schema=schema[3], if_exists="replace")
print("Loaded {}".format( table_id ))

if __name__ == "__main__":
    use_logging_handler()
  