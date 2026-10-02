
from playwright.sync_api import Page,expect
from locators import login_locators as locate
from utils import  data


def open_website(page:Page):
    page.goto("https://www.saucedemo.com/")

def assert_login(page,selector,value):
    expect(page.locator(locate.error_locator)).to_have_text(data.error)

def assert_output(actual,expected):
    assert expected==actual
