
from playwright.sync_api import Page,expect
from locators import login_locators as lc
from helper import  data as constants


def open_website(page:Page):
    page.goto("https://www.saucedemo.com/")

def assert_login(page,selector,value):
    expect(page.locator(lc.error_locator)).to_have_text(constants.error)

def assert_output(actual,expected):
    assert expected==actual
