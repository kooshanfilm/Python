from behave import *
from selenium import webdriver

# alows steps to recive argument from
# secnario
use_step_matcher('re')


@given('im on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/')


@when('I click on the line with id "blog-link"')
def step_impl(context):
 link = context.browser.find_element_by_id('blog-link')
 link.click()
 #time.sleep(2)

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

@given('im on the blogpage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/blog')

@when('I click on the line with id "home-link"')
def step_impl(context):
 link = context.browser.find_element_by_id('home-link')
 link.click()
 #time.sleep(2)

@then('I am on the HomePage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url