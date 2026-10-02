import pytest
from playwright.sync_api import Page, expect
from helper import data as constants
from helper import utils as hp
from locators import login_locators as lc
from pages import login_page

@pytest.mark.smoke
def test_login(page:Page):
    hp.open_website(page)
    login_page.login_valid(page)
    assert "inventory" in page.url

@pytest.mark.regression
def test_invalid_username(page:Page):
    hp.open_website(page)
    login_page.login_invalid_username(page)
    hp.assert_login(page,lc.error_locator,constants.error)

@pytest.mark.regression
def test_invalid_password(page:Page):
    hp.open_website(page)
    login_page.login_invalid_password(page)
    text=page.locator(lc.error_locator).text_content()
    hp.assert_output("Epic sadface: Username and password do not match any user in this service",text)

@pytest.mark.regression
def test_blank_value(page:Page):
    hp.open_website(page)
    login_page.login_blank(page)
    expect(page.locator(lc.error_locator)).to_have_text(constants.blank_error)












