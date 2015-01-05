#! /usr/bin/python
# Written By Tom Paulus, @tompaulus, www.tompaulus.com

from fancyhands import FancyhandsClient
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


def call_and_react(phone_number):
    """
    Call phone_number and prank them, then get their reaction

    :param phone_number: The Phone Number of who should be called
    :type phone_number: str
    :return:If it was successful
    :rtype: bool
    """

    title = "Prank call my friend!"
    description = "Call %s. Ask if their refrigerator is running." \
                  "When they say 'yes', tell them 'Well you better go catch it!'."
    bid = 3.00
    expiration_date = datetime.now() + timedelta(1)

    custom_fields = [
        {
            'label': 'Response',
            'type': 'textarea',
            'description': 'Their response to the prank. Please be as descriptive as possible. '
                           'Do not say "Competed call as requested. Thanks!',
            'order': 1,
            "required": True
        }
    ]

    client.custom_create(title, description % phone_number, bid, expiration_date, custom_fields)
    return True


print("Make Sure that the WebHooks URL on the Dashboard is up-to-date")
call_and_react("(555) 555-555")