import os
import pytest
import ansibleawx
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")
API_URL = os.getenv("API_URL")

@pytest.fixture()
def api():
    """
    Instance of Ansible AWX Client by username and password

    Returns:
        api: api client
    """
    api = ansibleawx.Api(username=USERNAME, password=PASSWORD, api_url=API_URL)
    return api

@pytest.fixture()
def api_token():
    """
    Instance of Ansible AWX Client by token

    Returns:
        api: api client
    """
    api = ansibleawx.Api(api_url=API_URL, token=TOKEN)
    return api