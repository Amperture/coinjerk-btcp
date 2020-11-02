import requests
from pprint import pprint


class StreamElementsJWTClient:
    user_id = ""
    jwt_token = ""

    BASE_HEADERS = {
            'accept': "application/json",
            'content-type': "application/json"
            }

    BASE_URL = "https://api.streamelements.com/kappa/v2/"

    ACCEPTED_CURRENCIES = [
            "AUD",
            "BRL",
            "CAD",
            "CZK",
            "DKK",
            "EUR",
            "HKD",
            "HUF",
            "ILS",
            "JPY",
            "MYR",
            "MXN",
            "NOK",
            "NZD",
            "PHP",
            "PLN",
            "GBP",
            "RUB",
            "SGD",
            "SEK",
            "CHF",
            "TWD",
            "THB",
            "TRY",
            "USD",
            "INR",
            "UAH"
            ]
    # url = f"https://api.streamelements.com/kappa/v2/tips/{user_id}/"

    def __init__(self, user_id, jwt_token):
        self.user_id = user_id
        self.jwt_token = jwt_token

    def tip_alert(self, payload):
        """
        Sends a tip alert request to StreamElements, containing payload as
        defined.

        Payload is a dictionary and shall contain:
            'username': String
            'amount': numeric (float or int)
            'currency': String MUST BE ONE OF <ACCEPTED_CURRENCIES>
        """
        TIPS_ENDPOINT = f'{self.BASE_URL}tips/{self.user_id}/'
        try:
            amount = payload['amount']
            username = payload['username']
            currency = payload['currency']
        except KeyError:
            print("AMOUNT USERNAME OR CURRENCY NOT PROVIDED")
            return 1

        if currency not in self.ACCEPTED_CURRENCIES:
            print("CURRENCY NOT ACCEPTED BY STREAMELEMENTS")
            return 1

        headers = self.BASE_HEADERS
        headers['Authorization'] = f"Bearer {self.jwt_token}"
        data = {
                'user': {
                    # TODO: PLACEHOLDER EMAIL
                    'email': payload.get('email', 'amp@amperture.com'),
                    'username': username
                    },
                'provider': "CoinJerk",
                'message': payload.get('message', ''),
                'amount': amount,
                'currency': currency,
                'imported': True
                }

        response = requests.post(TIPS_ENDPOINT, headers=headers, json=data)

        if response.json()['status'] == 'success':
            return 0
        else:
            return 1
