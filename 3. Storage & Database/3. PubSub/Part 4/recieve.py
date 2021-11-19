from google.cloud import pubsub_v1
import os
import logging
import google.cloud.logging
from google.cloud import bigquery

clientlogging = google.cloud.logging.Client()
clientlogging.setup_logging()


def logger(text):
    logging.info('text')
    print("Logged: {}".format(text))


def callback(message):
    with open(file, 'a') as f:
        f.write("Recieved " + str(message))
    logger("Received " + str(message))
    message.ack()


path = "/home/fagcpdebc1_09/pubsub/btcmp-1-69a235b69b1d.json"  # provide path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= path

project_id = "btcmp-1"

sub = int(input('select 1 for sub1 or 2 for sub2 '))
print(sub)
subscription_id = 'sub1' if 1 else 'sub2'
# Number of seconds the subscriber should listen for messages
timeout = 10.0

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path(project_id, subscription_id)

file_no = input('Enter 1 for file1 or 2 for file2 ')
file = 'file'+ str(file_no) + '.txt'


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
logger("Listening for messages on" + subscription_path + "..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.

