from behave import *
from selenium import webdriver

# alows steps to recive argument from
# secnario
use_step_matcher('re')


@given('im on the homepage')
def step_impl(context):
    browser = webdriver.chrome()
    browser.get('http://127.0.0.1:5000/')
