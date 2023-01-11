import unittest
from linkedin_scraper.ProfileScraper import ProfileScraper


class TestProfileScraper(unittest.TestCase):
    def test_get_intro_ok(self):
        ps = ProfileScraper()

        page = ps.get_profile_page("bmdnsoumia")

        scraped = ps.get_intro(page)
        print(scraped)
        expected = {'Name': 'Soumia BOUMEDDANE',
                    'Headline': 'PhD | Data Science | IoT',
                    'Current_company': 'Independant',
                    'Education': "Ecole nationale Superieure d'Informatique (ESI)",
                    'Location': 'location'}
        # +++ more test cases : profiles with/without location, education and current company sections ...
        self.assertTrue(scraped == expected)

    def test_get_intro_except(self):
        pass
