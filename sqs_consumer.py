import json
import logging

import boto3

from sqs_producer import find_queue

logger = logging.getLogger(__name__)
sqs = boto3.client("sqs", endpoint_url='http://localhost:4566')


def consume_message(queue_name):
    queue = find_queue(queue_name)

    message = sqs.receive_message(
        QueueUrl=queue['QueueUrl']
    )

    if 'Messages' not in message:
        return False

    msg = message['Messages']
    msg = msg[0]

    rcpt_handle = msg['ReceiptHandle']
    msg = msg['Body']

    msg = json.loads(msg)

    print(msg)

    sqs.delete_message(
        QueueUrl=queue['QueueUrl'],
        ReceiptHandle=rcpt_handle
    )

    return True


if __name__ == '__main__':
    while consume_message('test_test'):
        continue
