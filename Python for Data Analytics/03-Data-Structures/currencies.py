# pylint: disable=missing-docstring

RATES = {"USDEUR":0.85,"GBPEUR":1.13,"CHFEUR":0.86,"EURGBP":0.885, "PENEUR": 0.25}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    # pass  # YOUR CODE HERE
    for key, value in RATES.items():
        if amount[1] + currency == key:
            return round(amount[0] * value)
    return None
