import requests
from utilities.configurations import *
from utilities.resoures import APIReferences
from behave import given, when, then

@given('establish the server connection')
def delete_user_url(context):
    config1 = get_configurations()
    context.url = config1.get('API','base_url') + APIReferences.delete_book
    context.headers = get_header()
@when('send the request')
def delete_user(context):
    context.response = requests.delete(context.url, headers=context.headers)

@then('validate the result')
def validate_delete_user(context):
    assert context.response.status_code == 204

