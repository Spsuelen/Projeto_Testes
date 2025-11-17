from BasePage import BasePage
from ValidatorExpense import ValidatorExpense
import time

class EditExpense(BasePage):

    expense_price_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/etPrice"}
    expense_done_button_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/fabDone"}
    reports_title_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/textViewRecords"}

    def edit_specific_expense(self, new_price):
        expense_price = self.device(**self.expense_price_locator)
        expense_price.clear_text()
        expense_price.set_text(new_price)

        expense_done_button = self.device(**self.expense_done_button_locator)
        expense_done_button.click()

        ValidatorExpense.validate_price(new_price)

        self.device(**self.expense_done_button_locator).wait_gone(timeout=10.0)