import pytest
from playwright.sync_api import Page
from helper import utils as help
from pages import inventory_page


@pytest.mark.smoke
def test_product(page:Page):
    help.open_website(page)
    inventory_page.product_page(page)
    assert "inventory" in page.url

def test_sort_asc(page:Page):
    help.open_website(page)
    inventory_page.product_page(page)
    page.locator('//select[@data-test="product-sort-co ntainer"]/option[@ value="az"]').click()
    page.locator('span[data-test="active-option"]').text_content()
    # hp.assert_output('Name (A to Z)',text)





