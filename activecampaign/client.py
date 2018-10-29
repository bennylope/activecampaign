"""
The client module is responsible for abstracting away connecting to, making
requests to, and serializing responses from the ActiveCampaign API.
"""

import requests

from .contacts import Contacts


class ActiveCampaignClient(object):

    def __init__(self, host, key):
        """
        Requests are issued against an account specific domain
        """
        if not host.startswith("http"):
            self.host = "https://" + host
        else:
            self.host = host
        self.key = key
        self.contacts = Contacts(self)

    def request(self, method, action, data=None):
        """

        Args:
            method: the HTTP method to use as an uppercase string
            action: the name of the URL parameter defining the API action
            data: a list of tuples for the data. Used in lieu of a dictionary to allow
                    for key duplication

        Returns:

        """
        url = "{0}/admin/api.php".format(self.host)
        params = [("api_action", action), ("api_key", self.key), ("api_output", "json")]
        if method in ("GET", "DELETE"):
            if data is not None:
                params += data
            data = []
        else:
            data = data

        response = requests.request(method, url, params=params, data=data)
        return response
