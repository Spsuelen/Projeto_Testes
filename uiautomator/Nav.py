import uiautomator2 as u2
from BasePage import BasePage


class Navigation(BasePage):

    expenses_navigation = {'description': 'Open navigation drawer'}

    expenses_results = {'xpath': '//android.widget.CheckedTextView[@resource-id='
                                 '"com.blogspot.e_kanivets.moneytracker:'
                                 'id/design_menu_item_text" and @text="Results"]'}

    list_nav_summary = {'text': 'SUMMARY'}

    list_nav_graph = {'text': 'GRAPH'}

    def list_to_navigation(self):
        self.device(**self.expenses_navigation).click(timeout=30.0)

    def list_to_results(self):
        xpath_selector = self.expenses_results.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)

    def list_expenses_summary(self):
        self.device(**self.list_nav_summary).click(timeout=30.0)

    def list_expenses_graph(self):
        self.device(**self.list_nav_graph).click(timeout=30.0)