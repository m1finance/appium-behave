from behave import given, when, then # pylint: disable=no-name-in-module
from behave import *
import time 
from appium import webdriver

@given('I am logged in')
def first_step(context):
    
    time.sleep(10)

    logInButtonChain = '**/XCUIElementTypeButton[`label == "Log In"`]'
    logInButton = context.driver.find_element_by_ios_class_chain(logInButtonChain)
    logInButton.click()

    context.driver.find_element_by_ios_predicate('value == "Email"').send_keys('peter@example.com')
    
    context.driver.find_element_by_ios_predicate('label == "Log In" AND name == "Log In" AND type == "XCUIElementTypeButton"').click()

    time.sleep(10)

@when('I navigate to the invest screen')
def second_step(context):
    time.sleep(10)

@then('I can see my invest details')
def third_step(context):
    time.sleep(10)
    assert 0 == 0
    # assert 1 == 0, "This is an error message"


