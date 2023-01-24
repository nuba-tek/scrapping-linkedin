"""

"""
import json

from botocore.exceptions import ClientError

from linkedin_scraper.helpers.s3_client import S3Client
import logging


class Profile:
    def __init__(self, profile_id, intro, experience=None, education=None, skills=None, licenses=None, publications=None, projects=None):
        self.profile_id = profile_id
        self.intro = intro
        self.experience = experience
        self.education = education
        self.skills = skills
        self.licenses = licenses
        self.publications = publications
        self.projects = projects

    def save_profile(self):
        profile_json = json.dumps(self.__dict__).encode('UTF-8')
        try:
            S3Client().put_object(body=bytes(profile_json), object_key='test/{0}.json'.format(self.profile_id))
        except ClientError as e:
            logging.error(e)