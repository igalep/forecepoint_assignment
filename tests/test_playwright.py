import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.playwright.pom.button_section import ButtonSection
from src.playwright.pom.href_section import HrefSection
from src.playwright.pom.form_section import FormSection


class TestAssignment:
    #Fills the form and retrieves the captcha answer.
    def fill_form_get_captcha(self, fs, first_name, last_name, email, message=''):
        fs.fill_form(first_name, last_name, email, message)
        captcha_ans = fs.parse_captcha()

        return captcha_ans

    #Test the count of buttons in the button section.
    @pytest.mark.positive
    def test_count_buttons(self, setup):
        bs = ButtonSection(setup)
        size = bs.count_buttons()
        assert size == 12

    #Test the count of hrefs in the href section.
    @pytest.mark.positive
    def test_count_href(self, setup):
        hrf = HrefSection(setup)

        li_count = hrf.count_li()
        x_count = hrf.count_x()
        all_counter = hrf.count_all()
        assert li_count + x_count == all_counter

        x_link_expected = 'https://x.com/forcepointsec'
        li_link_expected = 'https://www.linkedin.com/company/forcepoint/'
        hrf_counter_li = 0
        hrf_counter_x = 0

        for i in range(all_counter):
            hrf_link = hrf.get_hrf_link(hrf.href_all.nth(i))
            if hrf_link == x_link_expected:
                hrf_counter_x += 1
            elif hrf_link == li_link_expected:
                hrf_counter_li += 1

        assert all_counter == hrf_counter_x + hrf_counter_li


    #Test the form section with the intercept response.
    @pytest.mark.parametrize('first_name,last_name,email',[
        ('Donald', 'Duck' ,'donald@duck.com')
        ])
    @pytest.mark.positive
    def test_fill_form_intercept(self, intercept_response, first_name, last_name, email):
        page, captcha_correct_response = intercept_response

        fs = FormSection(page)
        fs.fill_form(first_name, last_name, email)
        fs.fill_captcha_ans(captcha_correct_response)
        fs.submit_form()

        captcha_message = fs.get_output_message_success()

        assert first_name in captcha_message
        assert last_name in captcha_message


    #Test the form section with captcha parsing. (Positive)
    @pytest.mark.parametrize('first_name,last_name,email, message, response_message',[
        ('Miki', 'Mouse' ,'miki@mouse.com', 'Hello World', 'Thank you, {} {}! Your submission is successful.')
    ])
    @pytest.mark.positive
    def test_fill_form_right_captcha(self, setup, first_name, last_name, email, message, response_message):
        fs = FormSection(setup)

        captcha_ans = self.fill_form_get_captcha(fs, first_name, last_name, email, message)

        assert captcha_ans != []

        fs.fill_captcha_ans(str(sum(captcha_ans)))

        fs.submit_form()
        captcha_message = fs.get_output_message_success()

        assert captcha_message == response_message.format(first_name,last_name)

    #Test the form section with captcha parsing. (Negative)
    @pytest.mark.parametrize('first_name,last_name,email, response_message',[
        ('Bugs', 'Bunny' ,'bugs@bunny.com', 'Incorrect answer to the captcha. Please try again.')
    ])
    @pytest.mark.negative
    def test_fill_form_wrong_captcha(self, setup, first_name, last_name, email, response_message):
        fs = FormSection(setup)

        captcha_ans = self.fill_form_get_captcha(fs, first_name, last_name, email)

        assert captcha_ans != []

        fs.fill_captcha_ans(str(sum(captcha_ans) + 1))

        fs.submit_form()
        captcha_message = fs.get_output_message_failure()

        assert captcha_message == response_message

    #Test the form section with partial fields and validate native browser's errors. (Negative)
    @pytest.mark.parametrize('first_name,last_name,email, form_error_message, locator_name', [
        ('', 'Bunny', 'bugs@bunny.com', 'Please fill out this field.', 'first_name'),
        ('Bugs', 'Bunny', 'bunny.com', 'Please include an \'@\' in the email address.', 'email'),
    ])
    @pytest.mark.negative
    def test_fill_form_partial_fields(self, setup, first_name, last_name, email, form_error_message, locator_name):
        fs = FormSection(setup)

        captcha_ans = self.fill_form_get_captcha(fs, first_name, last_name, email)

        assert captcha_ans != []

        fs.fill_captcha_ans(str(sum(captcha_ans)))

        fs.submit_form()
        error_message = fs.get_form_native_error_message(locator_name)

        assert form_error_message in error_message


