# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    # pass  # YOUR CODE HERE
    response = requests.get(f'https://opengraph.lewagon.com/?url={url}')
    if response.status_code != 200:
        return ""
    return response.json()['data']

# To manually test, please uncomment the following lines and run `python opengraph.py`:
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))
