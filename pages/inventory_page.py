from playwright.sync_api import Page
from locators import login_locators as lc
from helper import actions_for_pages as ap
from helper import data as constants


def product_page(page:Page):
    ap.fill_action(page,lc.username,constants.valid_username)
    ap.fill_action(page,lc.password,constants.valid_password)
    ap.click_action(page,lc.submit)