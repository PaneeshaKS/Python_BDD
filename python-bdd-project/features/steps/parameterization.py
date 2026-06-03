import requests
from utilities.configurations import *
from utilities.resoures import APIReferences
from behave import given, when, then


@given('Form the dataset for the post request')
def step_impl(context):
    pass

@when("establish the connection with the database by providing {firstname}, {lastname}, {age}")
def config_server(context,firstname, lastname, age):
    pass

@then("verify the given result")
def verify_result(context):
    pass