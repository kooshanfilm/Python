from behave import *
from tests.acceptance.locators.home_page import HomePageLocators

use_step_matcher('re')



@then('there is a title shown on the page')
def step_impl(context):
    title_tag = context.browser.find_element(*HomePageLocators.title)
    assert title_tag.is_displayed()


@step('the title tag content "This is the blog page"')
def step_impl(context):
    title_tag = context.browser.find_element(*HomePageLocators.title)
    assert title_tag.text == "This is the blog page"
