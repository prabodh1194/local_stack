import logging
import boto3

logger = logging.getLogger(__name__)


sqs = boto3.resource("sqs")