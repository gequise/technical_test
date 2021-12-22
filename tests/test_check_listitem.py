from tests.misc.BrowserSetup import BrowserSetup
from tests.pages.HomePage import Homepage


class TestCheckListItem:

    def set_up(self):
        self.browser = BrowserSetup()
        self.tp = Homepage(self.browser.get_driver())

    def tear_down(self):
        self.browser.close_driver()

    def test_checklistitem(self):
        self.set_up()
        list_items = self.tp.check_listitem()
        assert 'Creators: Matt Duffer, Ross Duffer' in list_items, 'Exist element in list'
        self.tear_down()
