import unittest
from moto import mock_s3
from moto.s3.responses import DEFAULT_REGION_NAME

from linkedin_scraper.helpers.s3_client import S3Client


@mock_s3
class TestS3Client(unittest.TestCase):
    mock_s3 = mock_s3()
    bucket_name = "TestBucket"

    def setUp(self):
        self.mock_s3.start()
        self.my_client = S3Client(region_name=DEFAULT_REGION_NAME)
        s3 = self.my_client.s3_resource
        bucket = s3.Bucket(self.bucket_name)
        bucket.create()

    def tearDown(self):
        self.mock_s3.stop()

    def test_put_object(self):
        content = b"hello"
        key = "test/file.txt"

        self.my_client.put_object(content, bucket_name=self.bucket_name, object_key=key)

        object = self.my_client.s3_resource.Object(bucket_name=self.bucket_name, key=key)
        actual = object.get()["Body"].read()
        self.assertEqual(actual, content)
