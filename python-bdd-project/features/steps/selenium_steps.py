from behave import given, when, then
from utilities.selenium_driver import get_driver
from selenium.webdriver.common.by import By
from utilities.configurations import *

@given('Configure Driver and url of the website')
def configure_driver(context):
    context.driver = get_driver()
    context.driver.get(get_url())
    context.driver.maximize_window()

@when('perform the action')
def perform_action(context):
    element = context.driver.find_element(By.XPATH, "//*[@id='about']/a")
    element.click()

@then('validate the result and close the brower')
def validate_and_close(context):
    assert "Python" in context.driver.title
    #after_scenario(context, None)  # Close the browser after validation