import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit,
                         headers=data.headers)