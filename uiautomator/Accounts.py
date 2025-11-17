import uiautomator2 as u2
from BasePage import BasePage


class Accounts(BasePage):

    expenses_navigation = {'description': 'Open navigation drawer'}

    expenses_accounts = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/design_menu_item_text',
                         'text': 'Accounts'}

    expenses_btn_accounts = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/btn_add_account'}
    expenses_btn_add = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/action_done'}


    def list_to_navigation(self):
        self.device(**self.expenses_navigation).click(timeout=30.0)

    def list_to_accounts(self):
        self.device(**self.expenses_accounts).click(timeout=30.0)

    def list_to_btn_accounts(self):
        self.device(**self.expenses_btn_accounts).click(timeout=30.0)

    def list_to_btn_add(self):
        self.device(**self.expenses_btn_add).click(timeout=30.0)