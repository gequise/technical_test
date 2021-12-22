from tests.misc.BrowserSetup import BrowserSetup
from tests.pages.HomePage import Homepage


class TestDeleteCreated:

    def set_up(self):
        self.browser = BrowserSetup()
        self.tp = Homepage(self.browser.get_driver())

    def tear_down(self):
        self.browser.close_driver()

    def test_deletecreated(self):
        self.set_up()
        self.tp.delete_last_item()
        self.tear_down()
