import json

from bs4 import BeautifulSoup
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from linkedin_scraper.Profile import Profile
from linkedin_scraper.LinkedinScraper import LinkedinScraper
from selenium.webdriver.support import expected_conditions as EC
import logging

from linkedin_scraper.helpers.s3_client import S3Client

"""

"""


class ProfileScraper(LinkedinScraper):

    def scrape(self, profile_id):
        """

        :param profile_id: Linkedin profile's ID
        :return: profile details as a dict
        """
        try:
            page = self.get_profile_page(profile_id)

            intro = self.get_intro(page)

            profile = Profile(intro=intro)
            profile_json = json.dumps(profile.__dict__).encode('UTF-8')
            S3Client().put_object(body=bytes(profile_json), object_key='test/profile.txt')

            return profile
        except WebDriverException as e:
            logging.error(str(e))
            return

    def get_profile_page(self, profile_id):
        """

        :param profile_id:
        :return:
        """
        try:
            profile_url = 'https://www.linkedin.com/in/{}'.format(profile_id)
            self.driver.get(profile_url)
            try:
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.ID, "profile-content")))
            except TimeoutException as e:
                logging.error(str(e))
                raise ValueError("Profile not found")
            self.driver.implicitly_wait(20)

            src = self.driver.page_source
            page = BeautifulSoup(src, 'html.parser')
            return page
        except WebDriverException as e:
            logging.error(str(e))
            raise WebDriverException

    def get_intro(self, page):
        """
        Get profil intro : name, headline, education, current company
        :param page: page html
        :return: dict containig : "Name", "Headline", "Education", "Current company"
        """
        name = ''
        headline = ''
        education = ''
        current_company = ''
        try:
            intro_div = page.find('div', {'class': 'pv-text-details__left-panel'})
            if intro_div is not None:
                name_h1 = intro_div.find("h1")
                name = name_h1.get_text().strip()
            else:
                logging.warning("")

            headline_div = intro_div.find("div", {'class': ['text-body-medium', 'break-words']})
            if headline_div is not None:
                headline = headline_div.get_text().strip()

            details_ul = page.find('ul', {'class': 'pv-text-details__right-panel'})
            if details_ul is not None:
                for li in details_ul.find_all("li"):
                    btn = li.find("button")
                    if btn.has_attr("aria-label"):
                        if btn['aria-label'].startswith('Education'):
                            education = li.text.strip()
                        if btn['aria-label'].startswith('Current company'):
                            current_company = li.text.strip()

            return {"Name": name,
                    "Headline": headline,
                    "Current_company": current_company,
                    "Education": education,
                    "Location": "location"}
        except AttributeError as e:
            logging.error(e)

    def get_About(self, page):
        """

        :return:
        """
        div_about_head = page.find('div', {'id': 'about'})
        pr = div_about_head.parents

        return

    def scrap_experience(self, page):
        """

        :return:
        """
        div_experience_head = page.find('div', {'id': 'experience'})
        return

    def get_education(self):
        """

        :return:
        """
        return

    def scrap_skills(self):
        """

        :return:
        """
        return

    def scrap_licenses(self):
        """

        :return:
        """
        return

    def scrap_publications(self):
        """

        :return:
        """
        return

    def scrap_projects(self):
        """

        :return:
        """
        return
