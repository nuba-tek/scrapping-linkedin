from bs4 import BeautifulSoup
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By

from LinkedinScraper import LinkedinScraper
import logging
import time
import random
from urllib.parse import urlparse, parse_qs

class SearchProfiles(LinkedinScraper):


    def search_profiles(self, first_name, last_name):
        """
        Return a list of linked profile urls
        :param fist_name:
        :param last_name:
        :return:
        """
        profiles_urls = []
        profiles_search_url = f'https://www.linkedin.com/search/results/people/?firstName={first_name}&lastName={last_name}&origin=FACETED_SEARCH&sid=tUV'

        try:
            self.driver.get(profiles_search_url)
        except WebDriverException as e:
            logging.error(str(e))
            raise WebDriverException
        
        time.sleep(random.uniform(2.5, 4.9))
        
        number_of_pages = self.driver.find_elements(By.CLASS_NAME, "artdeco-pagination__indicator--number>button")
        
        if (len(number_of_pages) == 0):
            profiles_urls = self.scrape_profiles_urls(profiles_urls)
        else:
            for i in range(1, len(number_of_pages) + 1):
                profiles_urls = self.scrape_profiles_urls(profiles_urls)
                time.sleep(random.uniform(4, 5.9))
                next_btn = self.driver.find_element(By.CLASS_NAME, "artdeco-pagination__button--next")
                next_btn.click()
                time.sleep(random.uniform(4, 5.9))
        return profiles_urls

    def check_if_element_exists(self, class_name):
        try:
            self.driver.find_element(By.CLASS_NAME, class_name)
        except NoSuchElementException:
            return False
        return True


    def get_first_word_in_string(self, phrase):
        return phrase.split()[0]

    def get_profile_id_from_url(self, url):
        # Return the profile id from the query string of a url
        return (url.split("/"))[2]

    def scrape_profiles_urls(self, profiles_urls):
        
        profiles = self.driver.find_elements(By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)")

        for profile in profiles:
            parse_result = urlparse(profile.get_attribute("href")).path
            parse_result = self.get_profile_id_from_url(parse_result)
            profiles_urls.append(parse_result)
        return profiles_urls