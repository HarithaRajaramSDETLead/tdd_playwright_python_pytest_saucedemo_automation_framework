from playwright.sync_api import Page
from utils import data as constants
from utils import  actions_for_pages as ap
from locators import login_locators as locate


def login_valid(page:Page):
    ap.fill_action(page,locate.username,constants.valid_username)
    ap.fill_action(page,locate.password,constants.valid_password)
    ap.click_action(page,locate.submit)

def login_invalid_username(page:Page):
    ap.fill_action(page,locate.username,constants.invalid_username)
    ap.fill_action(page,locate.password,constants.valid_password)
    ap.click_action(page,locate.submit)

def login_invalid_password(page:Page):
    ap.fill_action(page, locate.username, constants.valid_username)
    ap.fill_action(page, locate.password, constants.invalid_password)
    ap.click_action(page, locate.submit)

def login_blank(page:Page):
    ap.fill_action(page,locate.username,constants.blank_un)
    ap.fill_action(page,locate.password,constants.blank_password)
    ap.click_action(page,locate.submit)


