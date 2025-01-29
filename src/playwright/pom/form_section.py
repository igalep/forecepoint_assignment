from playwright.sync_api import Locator, Page

class FormSection:
    def __init__(self, page : Page):
        self.page = page
        self.form_container : Locator = page.locator('.form-section')
        self.first_name = self.form_container.locator('#first_name')
        self.last_name = self.form_container.locator('input[name="last_name"]')
        self.email = self.form_container.locator('#email')
        self.message = self.form_container.locator('#message')

        self.captcha = self.form_container.locator('label[for="captcha"]')
        self.captcha_input = self.form_container.locator('#captcha')

        self.submit_button = self.form_container.locator('.form-actions button[type="submit"]')

        self.captcha_output_message = self.form_container.locator('.success-message')


    def fill_form(self, first_name, last_name, email, message=''):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.message.fill(message)

    def parse_captcha(self):
        captcha_inner = self.captcha.inner_text()
        captcha_values = [int(num) for num in captcha_inner.split() if num.isdigit()]

        if len(captcha_values) == 2:
            return captcha_values
        else:
            return []

    def fill_captcha_ans(self, ans):
        self.captcha_input.fill(ans)

    def submit_form(self):
        self.submit_button.click()

    def get_output_message(self):
        return self.captcha_output_message.inner_text()