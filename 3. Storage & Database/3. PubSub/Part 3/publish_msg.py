from google.cloud import pubsub_v1
import os
import logging
import google.cloud.logging
from google.cloud import bigquery

pub_path = "/home/fagcpdebc1_09/pubsub/btcmp-1-69a235b69b1d.json"  # provide path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= pub_path

logger_path = "/home/fagcpdebc1_09/pubsub/btcmp-1-492f18bb6e0c.json" # provide path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= logger_path

# TODO(developer)
project_id = "btcmp-1"
topic_id = "topic1"


def use_logging_handler():
    clientlogging = google.cloud.logging.Client()
    clientlogging.setup_logging()
    text = "executed!"
    logging.info(text)
    print("Logged: {}".format(text))

    
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = pub_path


publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)


for n in range(1, 10):
    data = ("Message number {}".format(n))
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())


print("Published messages to {}.".format(topic_path))


if __name__ == "__main__":
    use_logging_handler()









# clientlogging = google.cloud.logging.Client()
# clientlogging.setup_logging()

# def logger(text):
#     logging.info(text)
#     print("Logged: {}".format(text))

# publisher = pubsub_v1.PublisherClient()
# # The `topic_path` method creates a fully qualified identifier
# # in the form `projects/{project_id}/topics/{topic_id}`
# topic_path = publisher.topic_path(project_id, topic_id)

# for n in range(1, 10):
#     data = "Message number " + str(n)
#     # Data must be a bytestring
#     data = data.encode("utf-8")
#     # When you publish a message, the client returns a future.
#     future = publisher.publish(topic_path, data)
#     logger(future.result())

# logger("Published messages to " + topic_path)
