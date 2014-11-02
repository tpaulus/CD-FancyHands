#! /usr/bin/python
# Written By Tom Paulus, @tompaulus, www.tompaulus.com

from fancyhands import FancyhandsClient
from datetime import datetime, timedelta

api_key = ''
secret = ''

client = FancyhandsClient(api_key, secret)
""" Client is our interface to FancyHands Once we have initialized it, it will remember who we are thought the file """


def reddit(phone_number):
    """
    Get the top story off of or Reddit and have phone_number be called telling them the title
    :param phone_number: The Phone Number of who should be called
    :type phone_number: str
    """

    title = "Let me know what's new on the internet!"
    description = "Go to Reddit, and find the title of the top story. Call me at %s and tell me that title."
    # %s will be replaced with a phone number when we use the variable in a function call
    bid = 1.50
    expiration_date = datetime.now() + timedelta(1)

    client.standard_create(title, description % phone_number, bid, expiration_date)
    return True

reddit("(111) 111-1111")