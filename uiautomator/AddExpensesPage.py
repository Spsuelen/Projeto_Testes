from BasePage import BasePage
from ValidatorExpense import ValidatorExpense
from ValidadorCategory import ValidadorCategory
from ValidadorTitle import ValidadorTitle
from Data import TestData
from datetime import datetime
import time

class AddExpensesPage(BasePage):

    expense_price_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/etPrice"}
    expense_title_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/etTitle"}
    expense_category_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/etCategory"}
    expense_date_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/tvDate"}
    expense_confirm_date_locator = {"resourceId": "android:id/button1"}
    expense_time_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/tvTime"}
    expense_confirm_time_locator = {"resourceId": "android:id/button1"}
    expense_done_button_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/fabDone"}

    def expense_price(self, text):
        element = self.device(**self.expense_price_locator)
        element.clear_text()
        element.set_text(TestData.expense_price)
        ValidatorExpense.validate_price(TestData.expense_price)

    def expense_title(self, text):
        element = self.device(**self.expense_title_locator)
        element.clear_text()
        element.set_text(TestData.expense_title)
        ValidadorTitle.validate_title(TestData.expense_title)

    def expense_category(self, text):
        element = self.device(**self.expense_category_locator)
        element.clear_text()
        element.set_text(TestData.expense_category)
        ValidadorCategory.validate_category(TestData.expense_category)

    def expense_date(self):
        element = self.device(**self.expense_date_locator)
        element.click()

    def expense_confirm_date(self):
        element = self.device(**self.expense_confirm_date_locator)
        element.click()

    def expense_time(self):
        element = self.device(**self.expense_time_locator)
        element.click()

    def expense_confirm_time(self):
        element = self.device(**self.expense_confirm_time_locator)
        element.click()

    def expense_done_button(self):
        element = self.device(**self.expense_done_button_locator)
        element.click()