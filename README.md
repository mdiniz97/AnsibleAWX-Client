Ansible AWX Client
============

[![](https://img.shields.io/badge/python-3.4+-blue.svg)](https://www.python.org/download/releases/3.4.0/)  [![](https://img.shields.io/github/license/ResidentMario/missingno.svg)](https://github.com/mdiniz97/AnsibleAWX-Client/blob/master/README.md)


Donate to help keep this project maintained

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZHX5884XX26MW&source=url" target="_blank">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
</a>

Summary
-------

This is a unofficial python API client for Ansible AWX.

Requirements
------------
* requests

Quick Start Guide
-----------------

### Install Ansible AWX Client
	pip install ansibleawx-client

### Initialize API Client

You can do this with your username and password or using your Token.

#### Initialize client with your username and password

	import ansibleawx
    
    API_URL = "http://my-ansibleawx.com/api/v2"
    
    client = ansibleawx.Api("username", "password", api_url=API_URL)

#### Initialize client with your token
	import ansibleawx
    
    API_URL = "http://my-ansibleawx.com/api/v2"
    TOKEN = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    
    client = ansibleawx.Api(api_url=API_URL, token=TOKEN)

Examples
--------
#### Get Inventories
	
    # to get all inventories
    response = client.get_inventories()
    
    # to get specific inventory by id
    response = client.get_inventories(1)
    
#### Get Jobs Templates
	
    # to get all jobs templates
    response = client.get_jobs_templates()
    
    # to get specific job template by id
    response = client.get_jobs_templates(1)

#### Launch Job Template by id
	response = client.launch_job_template(1)

#### Relaunch Job by id
	response = client.relaunch_job(1)
    
#### Cancel Job by id
	response = client.cancel_job(1)

Function Reference
------------------

Consult the [Ansible Tower documentation](https://docs.ansible.com/ansible-tower/latest/html/towerapi/api_ref.html#/Authentication) for more details.
