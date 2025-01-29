class HrefSection:
    def __init__(self, page):
        self.page = page
        self.href_container = self.page.locator('.buttons .button-container')
        self.href_LI_list = self.href_container.locator('a[href*="linkedin.com"]')
        self.href_X_list = self.href_container.locator('a[href*="x.com"]')
        self.href_all = self.href_container.locator('a[href*=".com"]')

    # Counts the number of links containing 'linkedin.com' in the href attribute.
    def count_li(self):
        return  self.href_LI_list.count()

    # Counts the number of links containing 'x.com' in the href attribute.
    def count_x(self):
        return  self.href_X_list.count()

    #Counts the number of links containing '.com' in the href attribute.
    def count_all(self):
        return self.href_all.count()

    def get_hrf_link(self, locator):
        return locator.get_attribute('href')
