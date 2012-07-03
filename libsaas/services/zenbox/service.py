import json
import time

from libsaas import http, port
from libsaas.services import base

class Zenbox(base.Resource):
    """
    """
    def __init__(self, api_key):
        """
        Create a Zenbox service.

        :var api_key: API key
        :vartype api_key: str
        """
        self.api_key = api_key

    @base.apimethod
    def post_data(self, email, data):
        """
        Post data for an email address.

        Upstream documentation: {0}

        :var email: The email address to associate data with.
        :vartype event: str

        :var data: The data to post about your customer.
        :vartype properties: dict

        :return: A boolean that tells if the data was posted successfully.
        """

        params = {}
        params['api_key'] = self.api_key
        params['email']   = email
        params['data']    = json.dumps(data)

        request = http.Request('POST', 'https://zenboxapp.com/customers.json', params)
        request.nosign = True

        if not 200 <= code < 300:
            raise http.HTTPError(body, code, headers)

        return True