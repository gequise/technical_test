from tests.misc.BrowserSetup import BrowserSetup
from tests.pages.HomePage import Homepage


class TestCrateItem:

    def set_up(self):
        self.browser = BrowserSetup()
        self.tp = Homepage(self.browser.get_driver())

    def tear_down(self):
        self.browser.close_driver()

    def test_crateitem(self):
        self.set_up()
        self.tp.create_items()
        self.tear_down()
