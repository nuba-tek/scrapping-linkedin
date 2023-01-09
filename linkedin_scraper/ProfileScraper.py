from linkedin_scraper.Profile import Profile
from linkedin_scraper.LinkedinScraper import LinkedinScraper

"""

"""


class ProfileScraper(LinkedinScraper):

    def scrape(self, profile_id):
        """

        :param profile_id:
        :return:
        """
        try:
            profile_url = 'https://www.linkedin.com/in/{}'.format(profile_id)
            self.driver.get(profile_url)
            # profile = Profile()
            return "profile"
        except:
            return False

    def scrap_intro(self):
        """

        :return:
        """
        return

    def scrap_education(self):
        """

        :return:
        """
        return

    def scrap_experience(self):
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


ProfileScraper().scrape("bmdnsoumia")
