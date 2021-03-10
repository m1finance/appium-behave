from behave import given, when, then # pylint: disable=no-name-in-module
from behave import *
import time 
from appium import webdriver

@given('I am logged in')
def first_step(context):
    
    time.sleep(5)

    if context.driver.capabilities['platformName'] == 'Android':
        logInButton = context.driver.find_elements_by_class_name('Button')[0]
        logInButton.click()
        context.driver.find_elements_by_class_name('androidx.appcompat.widget.AppCompatAutoCompleteTextView')[0].clear()
        context.driver.find_elements_by_class_name('androidx.appcompat.widget.AppCompatAutoCompleteTextView')[0].send_keys('peter@example.com')

        context.driver.find_elements_by_class_name('androidx.appcompat.widget.AppCompatEditText')[0].clear()
        context.driver.find_elements_by_class_name('androidx.appcompat.widget.AppCompatEditText')[0].send_keys('test1234')

        time.sleep(1)
    
    elif context.driver.capabilities['platformName'] == 'iOS':
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


