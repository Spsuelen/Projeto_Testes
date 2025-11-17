import uiautomator2 as u2
from BasePage import BasePage


class Exchange(BasePage):

    expenses_navigation = {'description': 'Open navigation drawer'}

    expenses_exchange = {'xpath': '//android.widget.CheckedTextView[@resource-id='
                                  '"com.blogspot.e_kanivets.moneytracker:'
                                  'id/design_menu_item_text" and @text="Exchange rates"]'}

    expenses_btn = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/btn_add_exchange_rate'}

    expenses_add = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/action_done'}


    def list_to_navigation(self):
        self.device(**self.expenses_navigation).click(timeout=30.0)

    def list_to_exchange(self):
        xpath_selector = self.expenses_exchange.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)

    def list_to_btn_exchange(self):
        self.device(**self.expenses_btn).click(timeout=30.0)

    def list_to_btn_add(self):
        self.device(**self.expenses_add).click(timeout=30.0)