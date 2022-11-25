import datetime
import json
import logging
import boto3

logger = logging.getLogger(__name__)
sqs = boto3.client("sqs", endpoint_url='http://localhost:4566')


def find_queue(queue_name):
    queue = sqs.get_queue_url(QueueName=queue_name)
    return queue


def send_message(queue_name, cnt):
    queue = find_queue(queue_name)['QueueUrl']
    sqs.send_message(
        QueueUrl=queue,
        MessageBody=json.dumps({
            'a': cnt,
            'time': str(datetime.datetime.now())
        })
    )


if __name__ == '__main__':
    for i in range(10):
        send_message('test_test', i)
