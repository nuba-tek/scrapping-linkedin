"""

"""
import json

from botocore.exceptions import ClientError

from linkedin_scraper.helpers.s3_client import S3Client
import logging


class Profile:
    def __init__(self, profile_id, intro, experience=None, education=None, skills=None, licenses=None,
                 publications=None, projects=None):
        self.profile_id = profile_id
        self.intro = intro
        self.experience = experience
        self.education = education
        self.skills = skills
        self.licenses = licenses
        self.publications = publications
        self.projects = projects

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False).encode('UTF-8')

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    def save(self):
        try:
            S3Client().put_object(body=bytes(self.to_json()), object_key='test/{0}_{1}.json'.format(self.intro["name"], self.profile_id))
        except ClientError as e:
            logging.error(e)
