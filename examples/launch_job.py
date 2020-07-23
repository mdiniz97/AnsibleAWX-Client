import os
import ansibleawx
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")
API_URL = os.getenv("API_URL")

api = ansibleawx.Api(USERNAME, PASSWORD, API_URL)

r = api.launch_job_template(id=7)