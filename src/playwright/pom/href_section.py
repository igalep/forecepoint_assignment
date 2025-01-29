class HrefSection:
    def __init__(self, page):
        self.page = page
        self.href_container = self.page.locator('.buttons .button-container')
        self.href_LI_list = self.href_container.locator('a[href*="linkedin.com"]')
        self.href_X_list = self.href_container.locator('a[href*="x.com"]')
        self.href_all = self.href_container.locator('a[href*=".com"]')

    def count_li(self):
        return  self.href_LI_list.count()

    def count_x(self):
        return  self.href_X_list.count()

    def count_all(self):
        return self.href_all.count()

    def get_hrf_link(self, locator):
        return locator.get_attribute('href')
