from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException, JavascriptException, TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import time

"""

"""


class LinkedinScraper:

    def __init__(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            # options.add_argument('--user-agent')
            # options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_window_size(1920, 1080)

            self.driver.get("https://linkedin.com/uas/login")
            try:
                WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "username")))
            except TimeoutException as e:
                raise ValueError
            self.login(username="", password="1234567890")
            self.driver.implicitly_wait(20)
            time.sleep(20)
        except WebDriverException as e:
            logging.error(str(e))

    def login(self, username, password):
        """
        Authenticate to a Linkedin account using a username and password
        :param username: Linkedin account user name (email or phone number)
        :param password: Linkedin account's password
        :return:
        """
        try:
            username_input = self.driver.find_element(By.ID, "username")
            password_input = self.driver.find_element(By.ID, "password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

            # wait the ready state to be complete
            WebDriverWait(driver=self.driver, timeout=60).until(
                lambda x: x.execute_script("return document.readyState === 'complete'")
            )
            time.sleep(20)

            # get the errors (if there are)
            errors = self.driver.find_elements(By.CLASS_NAME, "form__label--error")

            if any(errors):
                logging.warning("Login failed")
            else:
                logging.info("Login successful")

        except (NoSuchElementException, JavascriptException) as e:
            logging.error(str(e))