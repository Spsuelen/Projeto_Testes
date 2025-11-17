import uiautomator2 as u2
from BasePage import BasePage


class ExpenseListPage(BasePage):
    expenses_reports = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/recyclerView'}
    list_expenses_button_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/spinner'}
    all_time_option_locator = {'xpath': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                        'android.widget.ListView/android.widget.TextView[5]'}
    day_time_option_locator = {'xpath': '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                        'android.widget.ListView/android.widget.TextView[1]'}

    def navigate_to_list_page_selector(self):
        self.device(**self.expenses_reports).click(timeout=10.0)

    def navigate_to_expense_list(self):
        self.device(**self.list_expenses_button_locator).click(timeout=30.0)

    def select_day_time_option(self):
        xpath_selector = self.day_time_option_locator.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)

    def select_all_time_option(self):
        xpath_selector = self.all_time_option_locator.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)