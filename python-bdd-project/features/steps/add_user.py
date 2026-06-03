import requests
from utilities.configurations import get_configurations, get_header
from utilities.resoures import APIReferences
from behave import given, when, then
from utilities.payload import add_user
from utilities.loger import setup_logger

logger = setup_logger()

@given("establish the server connection add")
def add_user_config(context):
    configure = get_configurations()
    context.url = configure.get('API', 'base_url') + APIReferences.add_user 
    context.headers = get_header()
    context.data = add_user()
    logger.info("URL: %s", context.url)
    logger.info("Headers: %s", context.headers)
@when("send the request add")
def add_user_url(context):
    context.response = requests.post(context.url, headers = context.headers, json = context.data)
    logger.info("Response Status Code: %s", context.response.status_code)
    logger.info("Response Body: %s", context.response.json())

@then("validate the result add")
def validate_add_user(context):
    assert context.response.status_code == 201
    assert context.response.json()['name'] == "morpheus"
    assert context.response.json()['job'] == "leader"
    logger.info("User added successfully with name: %s and job: %s", context.response.json()['name'], context.response.json()['job'])
    logger.info("Response validation successful")
    logger.debug("Response: %s", context.response.json())
