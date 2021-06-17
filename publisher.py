import os
from google.cloud import pubsub_v1

def what():
  print('What')
def publish_message():

  publisher = pubsub_v1.PublisherClient()
  topic_name = 'projects/{project_id}/topics/{topic}'.format(
      '12345',
      'TEST_TOPIC',
      # project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
      # topic='MY_TOPIC_NAME',  # Set this to something appropriate.
  )
  publisher.create_topic(name=topic_name)
  future = publisher.publish(topic_name, b'My first message!', spam='eggs')
  future.result()


what()
publish_message()

