from unittest import TestCase
import requests
import os

class api_testing(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.username = os.getenv('API_USER')
        cls.token = os.environ.get('API_TOKEN')
        cls.endpoint = 'https://api.github.com/repos/appanakarthik/login_use_cases/pulls'

    def setUp(self):
        self.gh_session = requests.Session()
        self.gh_session.auth = (self.username, self.token)

    def response_check(self):

        """To check whether api is getting response"""

        response = self.gh_session.get(self.endpoint)
        self.assertTrue(response.status_code==200, "response it self is failing")

    def check_pull_requests(self):

        """To get the  pull requests for the user specified"""

        pull_response = self.gh_session.get(self.endpoint)
        json_response = pull_response.json()
        self.assertTrue(json_response[0][u'labels'][0]['name'] == 'bug', "label is not displaying even though we "
                                                                         "have label ")

    def open_pull_requests(self):

        """To get the open  pull requests for the user specified"""
        op_response = self.gh_session.get(self.endpoint + '?state=open')
        json_response = op_response.json()
        self.assertTrue(json_response[0]['id'] == '645336051',"id is not generating for the open pull request")

    def closed_pull_requests(self):

        """To get the closed pull requests for the user specified"""

        op_res = self.gh_session.get(self.endpoint + '?state=closed')
        json_response = op_res.json()
        self.assertTrue(json_response[0]['id'] == '645327881',"id is not returning for the open pull request")

    def create_pull_requests(self):

        """To check created date is present for the open pull request"""

        op_res = self.gh_session.get(self.endpoint +'?sort=created&state=closed')
        create_response = op_res.json()
        self.assertTrue(create_response[0]['created_at'] == '2021-05-16T14:56:53Z',
                        "created date and time is not generating for the open pull request")

    def updated_pull_requests(self):

        """To check updated date time is present for the closed pull request"""

        op_res = self.gh_session.get(self.endpoint +'?sort=updated&state=closed')
        udpate_response = op_res.json()
        self.assertTrue(udpate_response[0][u'updated_at'] == '2021-05-16T14:56:53Z',
                        "updated date and time is not returned for the open pull request")

    # negative test case
    def page_pull_requests(self):

        """To pull requests per page that are open"""

        op_res = self.gh_session.get(self.endpoint +'?page=1&state=open')
        page_response = op_res.json()
        self.assertTrue(page_response != [], "pull requests are not showing even though we have")

    # negative test case
    def per_page_pull_requests(self):

        """To pull requests per page that are open"""

        response = self.gh_session.get(self.endpoint + '?per_page=2&state=closed')
        per_page = response.json()
        self.assertTrue(per_page==1, "this case should fail as per expectation ")