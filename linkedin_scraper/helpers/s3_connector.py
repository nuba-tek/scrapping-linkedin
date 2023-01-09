import boto3
from botocore.exceptions import ClientError
import logging


class S3Connector:
    def __init__(self):
        try:
            self.s3_ressource = boto3.resource(
                's3',
                region_name="eu-west-3",
                aws_access_key_id="AWS_ACCESS_KEY_ID",
                aws_secret_access_key="AWS_SECRET_ACCESS_KEY")
        except ClientError as e:
            logging.error(e)

    def load_object(self, file_name, bucket_name, object_key):
        """

        :param file_name:
        :param bucket_name:
        :param object_key:
        :return:
        """
        try:
            data = open(file_name, 'rb')
            self.s3_ressource.Object(bucket_name=bucket_name, key=object_key).put(Body=data)
            return True
        except FileNotFoundError as err:
            logging.error(err)
            return False
        except ClientError as e:
            logging.error(e)
            return False
