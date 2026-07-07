from playwright.sync_api import Page


class InventoryPage:
    """Page Object for the SauceDemo products/inventory screen."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def is_loaded(self) -> bool:
        return self.title.inner_text() == "Products"

    def add_item_to_cart(self, item_id: str = "sauce-labs-backpack") -> "InventoryPage":
        self.page.locator(f'[data-test="add-to-cart-{item_id}"]').click()
        return self

    def cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self) -> "InventoryPage":
        self.cart_link.click()
        return self
