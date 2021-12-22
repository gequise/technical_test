from tests.misc.BrowserSetup import BrowserSetup
from tests.pages.HomePage import Homepage


class TestCheckMaxLenght:

    def set_up(self):
        self.browser = BrowserSetup()
        self.tp = Homepage(self.browser.get_driver())

    def tear_down(self):
        self.browser.close_driver()

    def test_checkmaxlenght(self):
        self.set_up()
        self.tp.check_maxlenght()
        assert self.tp.get_attribute_create_btn() == 'true', "The btn disabled"
        self.tear_down()
