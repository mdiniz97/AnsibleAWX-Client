import os
import json
import requests
from base64 import b64encode
from ansibleawx.exceptions import (
    AuthError,
    UnauthorizedError,
    ParameterError,
    MissingParameterError,
)

from ansibleawx.decorators import require_auth


class Api(object):
    """
    Base Ansible AWX API class
    """

    def __init__(self, username=None, password=None, api_url=None, token=None):
        if api_url == None:
            raise MissingParameterError

        self._session = requests.Session()
        self.api_url = api_url
        self.headers = None

        if token:
            self.headers = {"Authorization": "Bearer {0}".format(token)}
        elif username and password:
            user_pass = "{0}:{1}".format(username, password).encode()
            user_pass_encoded = b64encode(user_pass).decode()
            self.headers = {"Authorization": "Basic {0}".format(user_pass_encoded)}
        else:
            raise MissingParameterError

        r = self._session.get(self.api_url + "/me/", headers=self.headers)

        if r.status_code == 403:
            raise UnauthorizedError
        elif r.status_code == 401:
            raise AuthError

    @require_auth
    def get_profile(self):
        r = self._session.get(self.api_url + "/me", headers=self.headers)
        return r.json()

    @require_auth
    def get_instances(self):
        r = self._session.get(self.api_url + "/instances/", headers=self.headers)
        return r.json()

    @require_auth
    def get_config(self):
        r = self._session.get(self.api_url + "/config/", headers=self.headers)
        return r.json()

    @require_auth
    def get_inventories(self, id=None):
        if id == None:
            r = self._session.get(self.api_url + "/inventories/", headers=self.headers)
        else:
            r = self._session.get(
                self.api_url + "/inventories/{0}".format(id), headers=self.headers
            )
        return r.json()

    @require_auth
    def create_inventory(self, **data):
        r = self._session.post(
            self.api_url + "/inventories/", headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def update_inventory(self, id, **data):
        r = self._session.patch(
            self.api_url + "/inventories/{0}/".format(id),
            headers=self.headers,
            json=data,
        )
        return r.json()

    @require_auth
    def delete_inventory(self, id):
        r = self._session.delete(
            self.api_url + "/inventories/{0}/".format(id),
            headers=self.headers,
            json=data,
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def get_hosts(self, id=None):
        if id == None:
            r = self._session.get(self.api_url + "/hosts/", headers=self.headers)
        else:
            r = self._session.get(
                self.api_url + "/hosts/{0}".format(id), headers=self.headers
            )
        return r.json()

    @require_auth
    def create_host(self, **data):
        if not data.get("name") or not data.get("inventory"):
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/hosts/", headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def update_host(self, id, **data):
        if not data.get("name") or not data.get("inventory"):
            raise MissingParameterError
        r = self._session.patch(
            self.api_url + "/hosts/{0}/".format(id), headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def delete_host(self, id):
        r = self._session.delete(
            self.api_url + "/hosts/{0}/".format(id), headers=self.headers
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def get_projects(self, id=None):
        if id == None:
            r = self._session.get(self.api_url + "/projects/", headers=self.headers)
        else:
            r = self._session.get(
                self.api_url + "/projects/{0}".format(id), headers=self.headers
            )
        return r.json()

    @require_auth
    def create_project(self, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/projects/", headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def update_project(self, id, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.patch(
            self.api_url + "/projects/{0}/".format(id), headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def delete_project(self, id):
        r = self._session.delete(
            self.api_url + "/projects/{0}/".format(id), headers=self.headers
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def sync_project(self, id):
        r = self._session.post(
            self.api_url + "/projects/{0}/update/".format(id), headers=self.headers
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def get_organizations(self, id=None):
        if id == None:
            r = self._session.get(
                self.api_url + "/organizations/", headers=self.headers
            )
        else:
            r = self._session.get(
                self.api_url + "/organizations/{0}".format(id), headers=self.headers
            )
        return r.json()

    @require_auth
    def create_organization(self, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/organizations/", headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def update_organization(self, id, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.patch(
            self.api_url + "/organizations/{0}".format(id),
            headers=self.headers,
            json=data,
        )
        return r.json()

    @require_auth
    def delete_organization(self, id):
        r = self._session.delete(
            self.api_url + "/organizations/{0}".format(id), headers=self.headers
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def get_jobs_templates(self, id=None):
        if id == None:
            r = self._session.get(
                self.api_url + "/job_templates/", headers=self.headers
            )
        else:
            r = self._session.get(
                self.api_url + "/job_templates/{0}".format(id), headers=self.headers
            )
        return r.json()

    @require_auth
    def create_job_template(self, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/job_templates/", headers=self.headers, json=data
        )
        return r.json()

    @require_auth
    def update_job_template(self, id, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.patch(
            self.api_url + "/job_templates/{0}/".format(id),
            headers=self.headers,
            json=data,
        )
        return r.json()

    @require_auth
    def delete_job_template(self, id):
        r = self._session.delete(
            self.api_url + "/job_templates/{0}/".format(id), headers=self.headers
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def get_job_template_survey_spec(self, id):
        r = self._session.get(
            self.api_url + "/job_templates/{0}/survey_spec/".format(id),
            headers=self.headers,
        )
        return r.json()

    @require_auth
    def create_job_template_survey_spec(self, id, **data):
        if not data.get("name"):
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/job_templates/{0}/survey_spec/".format(id),
            headers=self.headers,
            json=data,
        )
        return r.json()

    @require_auth
    def delete_job_template_survey_spec(self, id):
        r = self._session.post(
            self.api_url + "/job_templates/{0}/survey_spec/".format(id),
            headers=self.headers,
        )
        try:
            return r.json()
        except ValueError:
            return ""

    @require_auth
    def launch_job_template(self, id=None):
        if id == None:
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/job_templates/{0}/launch/".format(id), headers=self.headers
        )
        return r.json()

    @require_auth
    def get_jobs(self):
        r = self._session.get(self.api_url + "/jobs/", headers=self.headers)
        return r.json()

    @require_auth
    def get_job_summary(self, id=None):
        if id == None:
            raise MissingParameterError
        r = self._session.get(
            self.api_url + "/jobs/{0}/".format(id), headers=self.headers
        )
        return r.json()

    @require_auth
    def get_job_stdout(self, id=None, resp_format="json"):
        if id == None:
            raise MissingParameterError
        if resp_format not in [
            "html",
            "txt",
            "ansi",
            "json",
            "txt_download",
            "ansi_download",
        ]:
            raise ParameterError
        r = self._session.get(
            self.api_url + "/jobs/{0}/stdout/?format={1}".format(id, resp_format),
            headers=self.headers,
        )
        return r.text

    @require_auth
    def relaunch_job(self, id=None):
        if id == None:
            raise MissingParameterError
        r = self._session.post(
            self.api_url + "/jobs/{0}/relaunch/".format(id), headers=self.headers
        )
        return r.json()

    def cancel_job(self, id=None):
        if id == None:
            raise MissingParameterError

        canceled = False
        r = self._session.get(
            self.api_url + "/jobs/{0}/cancel/".format(id), headers=self.headers
        )
        if r.json()["can_cancel"]:
            r = self._session.post(
                self.api_url + "/jobs/{0}/cancel/".format(id), headers=self.headers
            )
            canceled = True
        return canceled
