#! /usr/bin/python
# Written By Tom Paulus, @tompaulus, www.tompaulus.com

from fancyhands import FancyhandsClient
# You can install the FancyHands API using pip: "sudo pip install fancyhands"
from datetime import datetime, timedelta


def read_api_keys(rel_file_path="./API.txt"):
    """
    Ignore this function, actually delete it before you run this file, all it does is try to open a file that contains
    the StudentRND API Key and Secret.

    :param rel_file_path: Location of the API Key File relative to the file being executed.
    :return fh_key: FancyHands API Key
    :return fh_secret: FancyHands API Secret
    :rtype : tuple

    """
    fh_key = ''
    fh_secret = ''

    try:
        with open(rel_file_path) as license_file:
            line = license_file.readline()

            while line != '':
                if line.count('Key:') == 1:
                    # Key Line
                    fh_key = line[5: -1]

                elif line.count('Secret:') == 1:
                    # Secret Line
                    fh_secret = line[8: -1]

                line = license_file.readline()  # Advance to the next line in the file.

    except IOError:
        print 'The API Key file does not exist. Not Fatal.'
        return None, None

    return fh_key, fh_secret
api_key, secret = read_api_keys()   # Delete this too.


# Uncomment the lines below and insert your API Key and Secret that you got from FancyHands
# api_key = ''
# secret = ''

client = FancyhandsClient(api_key, secret)
""" Client is our interface to FancyHands Once we have initialized it, it will remember who we are thought the file """


def reddit(phone_number):
    """
    Get the top story off of or Reddit and have phone_number be called telling them the title
    :param phone_number: The Phone Number of who should be called
    :type phone_number: str
    :return: If it was successful
    :rtype : bool
    """

    title = "Let me know what's new on the internet!"
    description = "Go to Reddit, and find the title of the top story. Call me at %s and tell me that title."
    # %s will be replaced with a phone number when we use the variable in a function call
    bid = 1.50
    expiration_date = datetime.now() + timedelta(1)

    client.standard_create(title, description % phone_number, bid, expiration_date)
    return True


reddit("(111) 111-1111")