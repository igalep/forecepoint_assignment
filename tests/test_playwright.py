import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.playwright.pom.button_section import ButtonSection
from src.playwright.pom.href_section import HrefSection
from src.playwright.pom.form_section import FormSection


class TestAssignment:
    def test_count_buttons(self, setup):
        bs = ButtonSection(setup)
        setup.screenshot(path='button.png')
        size = bs.count_buttons()
        assert size > 10


    def test_count_href(self, setup):
        setup.screenshot(path='href.png')
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


    def test_fill_form(self, setup):
        setup.screenshot(path='form.png')
        fs = FormSection(setup)

        fs.fill_form('aa', 'bb', 'aa@aa')
        fs.submit_form()
        setup.screenshot(path='form_err.png')

