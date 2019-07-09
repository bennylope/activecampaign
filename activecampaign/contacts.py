"""
The contacts module provides functionality for working with contacts in your
ActiveCampaign account.
"""

from activecampaign import http


class Contacts(object):

    def __init__(self, client):
        self.client = client

    def view(self, id):
        """
        Return an individual contact

        Args:
            id: an integer ID or email for a contact

        Returns:
            Dictionary of contact information
        """
        return self.client.request(http.GET, "contact_view", [("id", id)])

    def sync(self, **kwargs):
        if "email" not in kwargs:
            raise ValueError("You must include the email field")

        return self.client.request(http.POST, "contact_sync", kwargs)

    def tag_add(self, *tags, **kwargs):
        """
        Adds one or more tags to a contact

        The arguments `email` and `id` are mutually exclusive. If both are provided
        then only `id` will be used.

        Args:
            email: the email address of the ActiveCampaign contact
            id: the id of the ActiveCampaign contact
            *tags: list or iterable of string tag names

        Returns:

        """
        id = kwargs.pop("id", None)
        email = kwargs.pop("email", None)

        data = [("tags", tag) for tag in tags]
        if email is None and id is None:
            raise TypeError("Must provide `email` or `id` keyword argument")

        if id is not None:
            data.append(["id", id])
        else:
            data.append(["email", email])

        return self.client.request(http.POST, "contact_tag_add", data)

    def tag_remove(self, *tags, **kwargs):
        """
        Removes one or more tags from a contact

        The arguments `email` and `id` are mutually exclusive. If both are provided
        then only `id` will be used.

        Args:
            email: the email address of the ActiveCampaign contact
            id: the id of the ActiveCampaign contact
            *tags: list or iterable of string tag names

        Returns:

        """
        id = kwargs.pop("id", None)
        email = kwargs.pop("email", None)

        data = [("tags", tag) for tag in tags]
        if email is None and id is None:
            raise TypeError("Must provide `email` or `id` keyword argument")

        if id is not None:
            data.append(["id", id])
        else:
            data.append(["email", email])

        return self.client.request(http.POST, "contact_tag_remove", data)
