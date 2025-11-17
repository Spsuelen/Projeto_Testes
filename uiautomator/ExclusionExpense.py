from BasePage import BasePage

class ExclusionExpense(BasePage):
    reports_title_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/textViewRecords"}
    expense_delete_button_locator = {"resourceId": "com.blogspot.e_kanivets.moneytracker:id/action_delete"}

    def delete_expense(self):
        self.device(**self.expense_delete_button_locator).wait(timeout=10.0)

        self.device(**self.expense_delete_button_locator).click()

        self.device(**self.expense_delete_button_locator).wait_gone(timeout=10.0)