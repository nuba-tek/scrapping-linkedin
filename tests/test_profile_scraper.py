import unittest
from linkedin_scraper.ProfileScraper import ProfileScraper


class TestProfileScraper(unittest.TestCase):
    def setUp(self):
        self.ps = ProfileScraper()

    def tearDown(self):
        self.ps.driver.close()

    def test_get_intro_ok(self):
        page = self.ps.get_profile_page("bmdnsoumia")

        scraped = self.ps.get_intro(page)

        # self.ps.scrape("bmdnsoumia")

        print(scraped)
        expected = {'Name': 'Soumia BOUMEDDANE',
                    'Headline': 'PhD | Data Science | IoT',
                    'Current_company': '',  # 'Independant',
                    'Education': "",  # "Ecole nationale Superieure d'Informatique (ESI)",
                    'Location': 'location'}
        self.assertTrue(scraped == expected)

    def test_get_intro_except(self):
        pass
