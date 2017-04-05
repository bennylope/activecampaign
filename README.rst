=================
ActiveCampaign.py
=================


Simple and Pythonic ActiveCampaign API client

* Free software: BSD license

Features
--------

* View & sync a contact
* Add a contact tag
* Remove a contact tag

Basic usage
-----------

Initialize the client with your custom ActiveCampaign host name and API key::

    from activecampaign.client import ActiveCampaignClient
    client = ActiveCampaignClient(ACTIVECAMPAIGN_HOST, ACTIVECAMPAIGN_KEY)
    
Sync contact information::
    
    client.contacts.sync(
        email=customer_data['email'],
        first_name=customer_data['first_name'],
        last_name=customer_data['last_name'],
        orgname=custmoer_data['orgname'],
        phone=customer_data['phone'],
    )
    
Add and remove tags::

    client.contacts.tag_add("new-tag", email=customer_data['email'])
    client.contacts.tag_remove("old-tag", email=customer_data['email'])
