import pytest
from pytest_bdd import scenarios, given, when, then
import requests

scenarios('features\PostRequest.feature')

@given('Open the url')
def test_api_endpoint(context):
    context.headers = {
        "x-api-key": "reqres-free-v1"}
    context.url = "https://reqres.in/api/users"
    context.data = {
    "name": "morpheus",
    "job": "leader"
    }

@when('I perform an action')
def test_send_post_request(context):
    context.response = requests.post(context.url, json= context.data, headers=context.headers)
    return context.response
    return response

@then('I expect 200 response code')
def test_verify_response(context):
    assert context.response.status_code == 201

