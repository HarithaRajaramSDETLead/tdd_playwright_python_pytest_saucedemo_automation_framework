from playwright.sync_api import Page
from helper import data as constants
from helper import  actions_for_pages as ap
from locators import login_locators as lc


def login_valid(page:Page):
    ap.fill_action(page,lc.username,constants.valid_username)
    ap.fill_action(page,lc.password,constants.valid_password)
    ap.click_action(page,lc.submit)

def login_invalid_username(page:Page):
    ap.fill_action(page,lc.username,constants.invalid_username)
    ap.fill_action(page,lc.password,constants.valid_password)
    ap.click_action(page,lc.submit)

def login_invalid_password(page:Page):
    ap.fill_action(page, lc.username, constants.valid_username)
    ap.fill_action(page, lc.password, constants.invalid_password)
    ap.click_action(page, lc.submit)

def login_blank(page:Page):
    ap.fill_action(page,lc.username,constants.blank_un)
    ap.fill_action(page,lc.password,constants.blank_password)
    ap.click_action(page,lc.submit)


