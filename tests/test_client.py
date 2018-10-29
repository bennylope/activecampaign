#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_client
----------------------------------

Tests for `activecampaign.client` module.
"""

import unittest

from activecampaign import client


class TestClientSetup(unittest.TestCase):

    def test_schema(self):
        api_client = client.ActiveCampaignClient("https://blah.okay.com", "key")
        self.assertEqual(api_client.host, "https://blah.okay.com")

    def test_no_schema(self):
        api_client = client.ActiveCampaignClient("blah.okay-1.com", "key")
        self.assertEqual(api_client.host, "https://blah.okay-1.com")


if __name__ == "__main__":
    unittest.main()
