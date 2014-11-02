#! /usr/bin/python
# Written By Tom Paulus, @tompaulus, www.tompaulus.com

from fancyhands import FancyhandsClient
from datetime import datetime, timedelta

api_key = ''
secret = ''

client = FancyhandsClient(api_key, secret)


def call_and_react(phone_number):
    """
    Call phone_number and prank them, then get their reaction

    :param phone_number: The Phone Number of who should be called
    :type phone_number: str
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
            'description': 'Their response to the prank.',
            'order': 1,
            "required": True
        }
    ]

    client.custom_create(title, description % phone_number, bid, expiration_date, custom_fields)
    return True


call_and_react("(555) 555-555")