import random
import string
import requests
import json

aws_endpoint = {'url': 'http://ec2-52-28-4-254.eu-central-1.compute.amazonaws.com', 'users_path': '/users/'}


def rand_string_generator(length, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(length))


def rand_email_generator(length):
    return rand_string_generator(length % 3) + "@" + rand_string_generator(length % 3) + "." + rand_string_generator(
        length % 3)


class Requester(object):
    def __init__(self, params):
        self.base_url = params['url']
        self.users_path = params['users_path']

    def get_user(self, username):
        payload = {'requested_user': username}
        return requests.get(self.base_url + self.users_path + username, params=payload)

    def create_user(self, data, headers):
        return requests.post(self.base_url + self.users_path, data=data, headers=headers)

    def change_user(self, user_id, data, headers):
        return requests.patch(self.base_url + self.users_path + user_id, data=data, headers=headers)


class ExecuteData(object):
    def __init__(self, username, password, email, type_val="users",
                 content_type_var="application/vnd.api+json", user_id=""):
        self.username = username
        self.password = password
        self.email = email
        self.type_val = type_val
        self.content_type_var = content_type_var
        self.user_id = user_id

    def PostData(self):
        data = {
            "data": {
                "type": self.type_val,
                "attributes": {
                    "email": self.email,
                    "username": self.username,
                    "password": self.password
                }
            }
        }
        return json.dumps(data)

    def PatchData(self):
        data = {
            "data": {
                "type": self.type_val,
                "attributes": {
                    "username": self.username,
                }
            }
        }
        return json.dumps(data)

    def Header(self):
        content_type = {"Content-Type": self.content_type_var}
        return content_type


def Message(context, username, password, email):
    return "Error: " + context + "/n Current params: " + "username: " + username + "password: " + password + "email: " + email

test_requester = Requester(aws_endpoint)