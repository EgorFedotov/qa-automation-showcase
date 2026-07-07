"""UI tests for SauceDemo using Playwright and the Page Object Model."""
import allure
import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@allure.feature("SauceDemo UI")
@allure.story("Login")
def test_successful_login(page, ui_base_url, credentials):
    LoginPage(page).open(ui_base_url).login(
        credentials["username"], credentials["password"]
    )
    assert InventoryPage(page).is_loaded()
    assert "inventory.html" in page.url


@allure.feature("SauceDemo UI")
@allure.story("Login")
def test_locked_out_user_shows_error(page, ui_base_url):
    login = LoginPage(page).open(ui_base_url)
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_text().lower()


@allure.feature("SauceDemo UI")
@allure.story("Cart")
def test_add_single_item_updates_badge(page, ui_base_url, credentials):
    LoginPage(page).open(ui_base_url).login(
        credentials["username"], credentials["password"]
    )
    inventory = InventoryPage(page).add_item_to_cart("sauce-labs-backpack")
    assert inventory.cart_count() == 1


@allure.feature("SauceDemo UI")
@allure.story("Cart")
def test_cart_contains_added_item(page, ui_base_url, credentials):
    LoginPage(page).open(ui_base_url).login(
        credentials["username"], credentials["password"]
    )
    InventoryPage(page).add_item_to_cart("sauce-labs-backpack").open_cart()
    cart = CartPage(page)
    assert cart.items_count() == 1
    assert "Sauce Labs Backpack" in cart.names()
