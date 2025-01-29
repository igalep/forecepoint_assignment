from playwright.sync_api import Locator, Page

class FormSection:
    def __init__(self, page : Page):
        self.page = page
        self.form_container: Locator = page.locator('.form-section')

        #for reflection purposes
        self.first_name = '#first_name'
        self.first_name_locator = self.form_container.locator(self.first_name)
        self.email = '#email'
        self.email_locator = self.form_container.locator(self.email)

        self.last_name = self.form_container.locator('input[name="last_name"]')
        self.message = self.form_container.locator('#message')
        self.captcha = self.form_container.locator('label[for="captcha"]')
        self.captcha_input = self.form_container.locator('#captcha')

        self.submit_button = self.form_container.locator('.form-actions button[type="submit"]')

        self.captcha_output_message_success = self.form_container.locator('.success-message')
        self.captcha_output_message_failure = self.form_container.locator('.error-message')


    #Fills the form with the provided details.
    def fill_form(self, first_name, last_name, email, message=''):
        self.first_name_locator.fill(first_name)
        self.last_name.fill(last_name)
        self.email_locator.fill(email)
        self.message.fill(message)

    #Parses the captcha question and returns the two numbers as a list.
    def parse_captcha(self):
        captcha_inner = self.captcha.inner_text()
        captcha_values = [int(num) for num in captcha_inner.split() if num.isdigit()]

        if len(captcha_values) == 2:
            return captcha_values
        else:
            return []

    def fill_captcha_ans(self, captcha_ans):
        self.captcha_input.fill(captcha_ans)

    def submit_form(self):
        self.submit_button.click()

    def get_output_message_success(self):
        return self.captcha_output_message_success.inner_text()

    def get_output_message_failure(self):
        return self.captcha_output_message_failure.inner_text()

    # reflection on the attribute name in order to get evaluable locator and return native error message
    def get_form_native_error_message(self,locator_name):
        return self.page.eval_on_selector(getattr(self,locator_name), "el => el.validationMessage")