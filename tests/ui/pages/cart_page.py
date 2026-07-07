from playwright.sync_api import Page


class CartPage:
    """Page Object for the SauceDemo cart screen."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def items_count(self) -> int:
        return self.cart_items.count()

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()
