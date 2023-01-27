import unittest

from linkedin_scraper.Exceptions.ProfileExceptions import ProfileNotFoundException
from linkedin_scraper.ProfileScraper import ProfileScraper


class TestProfileScraper(unittest.TestCase):
    def setUp(self):
        self.ps = ProfileScraper()

    def tearDown(self):
        self.ps.driver.close()

    def test_get_profile_page_raise(self):
        with self.assertRaises(ProfileNotFoundException) as context:
            self.ps.get_profile_page("boumeddane_soumia")
        self.assertEqual("Linkedin profile not found", str(context.exception))

    def test_get_intro_ok(self):
        page = self.ps.get_profile_page("lilia-b-5a19a9195")

        scraped = self.ps.get_intro(page)

        # self.ps.scrape("bmdnsoumia")

        print(scraped)

        expected = {'name': 'Lilia B.',
                    'headline': "Étudiant(e) à Université M'Hamed Bougara de Boumerdes",
                    'current_company': '',
                    'education': "Université M'Hamed Bougara de Boumerdes",
                    'location': 'Algeria'}

        self.assertTrue(scraped == expected)

    def test_get_intro_raise(self):
        pass
