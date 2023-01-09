import argparse


def run_scraper(first_name, last_name, profile_id):
    """

    :param profile_id:
    :param first_name:
    :param last_name:
    :return:
    """
    if profile_id is not None:
        # run_scraper(profile_id=profile_id)
        print("Start scraping Linkedin account with profile_id={0}".format(profile_id))
    elif (first_name is not None) | (last_name is not None):
        # run_scraper(first_name=first_name, last_name=last_name)
        print("Start scraping Linkedin accounts with firstname={0} and lastname={1}".format(first_name, last_name))
    pass


parser = argparse.ArgumentParser(description="Linkedin scraper")
parser.add_argument("--firstname", "-f", help="fistname", required=False)
parser.add_argument("--lastname", "-l", help="lastname", required=False)
parser.add_argument("--profile_id", "-i", help="Linkedin profile Id", required=False)
parser.parse_args()

if __name__ == '__main__':
    try:
        args = parser.parse_args()
        fist_name = args.firstname
        last_name = args.lastname
        profile_id = args.profile_id

        run_scraper(fist_name, last_name, profile_id)
    except AttributeError as e:
        print(e)
