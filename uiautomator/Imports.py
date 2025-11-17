import uiautomator2 as u2
from BasePage import BasePage


class Imports(BasePage):

    expenses_navigation = {'description': 'Open navigation drawer'}

    expenses_imports = {'xpath': '//android.widget.CheckedTextView[@resource-id='
                                 '"com.blogspot.e_kanivets.moneytracker:'
                                 'id/design_menu_item_text" and @text="Import/Export"]'}

    expenses_info = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/action_help'}

    expenses_btn_ok = {'resourceId': 'android:id/button1'}

    expenses_btn_import = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/btn_import'}


    def list_to_navigation(self):
        self.device(**self.expenses_navigation).click(timeout=30.0)

    def list_to_import(self):
        xpath_selector = self.expenses_imports.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)

    def list_to_info(self):
        self.device(**self.expenses_info).click(timeout=30.0)

    def list_to_btn_ok(self):
        self.device(**self.expenses_btn_ok).click(timeout=30.0)

    def list_to_btn_import(self):
        self.device(**self.expenses_btn_import).click(timeout=30.0)