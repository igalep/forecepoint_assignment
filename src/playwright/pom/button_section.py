class ButtonSection:
    def __init__(self, page):
        self.page = page
        self.button_container = page.locator('.button-container')
        self.buttons_list = self.button_container.locator('.button')

    def count_buttons(self):
        """
        Counts the number of buttons in the button container.

        Returns:
            int:
        """
        return self.buttons_list.count()