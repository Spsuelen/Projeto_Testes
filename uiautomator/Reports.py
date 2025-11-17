import uiautomator2 as u2
from BasePage import BasePage


class Reports(BasePage):
    expenses_reports_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/recyclerView'}
    # list_expenses_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinner')
    add_expenses_button_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense'}

    def navigate(self):
        self.device(**self.expenses_reports_locator).wait(exists=True, timeout=20.0)

    def navigate_to_list_page(self):
        self.device(**self.expenses_reports_locator).click(timeout=20.0)

    def click_add_expenses_button(self):
        self.device(**self.add_expenses_button_locator).click(timeout=25.0)