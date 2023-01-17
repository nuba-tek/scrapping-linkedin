import boto3
from botocore.exceptions import ClientError
import logging

import config


class S3Client:
    def __init__(self,
                 region_name=config.REGION_NAME,
                 access_key_id=config.AWS_ACCESS_KEY_ID,
                 secret_access_key=config.AWS_SECRET_ACCESS_KEY):
        try:
            self.s3_resource = boto3.resource(
                's3',
                region_name=region_name,
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key)
        except ClientError as e:
            logging.error(e)

    def put_object(self, body, bucket_name=config.AWS_BUCKET_NAME, object_key=''):
        """
        Create an object in a existing S3 bucket
        :param body: Object content
        :param bucket_name: S3 bucket name
        :param object_key: Object key
        :return:
        """
        try:
            self.s3_resource.Object(bucket_name=bucket_name, key=object_key).put(Body=body)
            return True
        except ClientError as e:
            logging.error(e)
            return False
