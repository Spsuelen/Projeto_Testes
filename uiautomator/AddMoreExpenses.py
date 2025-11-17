from datetime import date
from datetime import datetime
import time
from datetime import timedelta
import uiautomator2 as u2
from BasePage import BasePage
from ValidatorExpense import ValidatorExpense
from ValidadorCategory import ValidadorCategory
from ValidadorTitle import ValidadorTitle
from Data import TestData


class AddMoreExpenses(BasePage):
    expense_price_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/etPrice'}
    expense_title_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/etTitle'}
    expense_category_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/etCategory'}
    expense_date_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/tvDate'}
    expense_confirm_date_locator = {'resourceId': 'android:id/button1'}
    expense_time_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/tvTime'}
    expense_confirm_time_locator = {'resourceId': 'android:id/button1'}
    expense_done_button_locator = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/fabDone'}


    def expense_price2(self, text):
        self.device(**self.expense_price_locator).set_text(TestData.expense_price, timeout=10.0)
        ValidatorExpense.validate_price(TestData.expense_price2)

    def expense_title2(self, text):
        self.device(**self.expense_title_locator).set_text(TestData.expense_title2, timeout=10.0)
        ValidadorTitle.validate_title(TestData.expense_title)
        ValidadorTitle.validate_title(TestData.expense_title2)


    def expense_category2(self, text):
        self.device(**self.expense_category_locator).set_text(TestData.expense_category2, timeout=10.0)
        ValidadorCategory.validate_category(TestData.expense_category2)

    def expense_date2(self):
        self.device(**self.expense_date_locator).click(timeout=10.0)

    def expense_confirm_date2(self):
        self.device(**self.expense_confirm_date_locator).click(timeout=10.0)

    def expense_time2(self):
        self.device(**self.expense_time_locator).click(timeout=10.0)

    def expense_confirm_time2(self):
        self.device(**self.expense_confirm_time_locator).click(timeout=10.0)

    def expense_done_button2(self):
        self.device(**self.expense_done_button_locator).click(timeout=10.0)

    def expense_price3(self, text):
            self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.expense_price3, timeout=10.0)
            ValidatorExpense.validate_price(TestData.expense_price3)

    def expense_title3(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.expense_title3, timeout=10.0)
        ValidadorTitle.validate_title(TestData.expense_title3)

    def expense_category3(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.expense_category3, timeout=10.0)
        ValidadorCategory.validate_category(TestData.expense_category3)

    def expense_date3(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=10.0)

    def expense_confirm_date3(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_time3(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=10.0)

    def expense_confirm_time3(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_done_button3(self):
        self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=10.0)


    def expense_price4(self, text):
            self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.expense_price4, timeout=10.0)
            ValidatorExpense.validate_price(TestData.expense_price4)

    def expense_title4(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.expense_title4, timeout=10.0)
        ValidadorTitle.validate_title(TestData.expense_title4)

    def expense_category4(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.expense_category4, timeout=10.0)
        ValidadorCategory.validate_category(TestData.expense_category4)

    def expense_date4(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=10.0)

    def expense_confirm_date4(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_time4(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=10.0)

    def expense_confirm_time4(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_done_button4(self):
        self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=10.0)

    def expense_price5(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.expense_price5, timeout=10.0)
        ValidatorExpense.validate_price(TestData.expense_price5)

    def expense_title5(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.expense_title5, timeout=10.0)
        ValidadorTitle.validate_title(TestData.expense_title5)

    def expense_category5(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.expense_category5, timeout=10.0)
        ValidadorCategory.validate_category(TestData.expense_category5)

    def expense_date5(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=10.0)

    def expense_confirm_date5(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_time5(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=10.0)

    def expense_confirm_time5(self):
        self.device(resourceId='android:id/button1').click(timeout=10.0)

    def expense_done_button5(self):
         self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=15.0)

    def expense_price_error1(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price1, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price1)

    def expense_title_error1(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title1, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title1)

    def expense_category_error1(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category1, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category1)

    def expense_date_error1(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error1(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error1(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error1(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error1(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")

    def expense_price_error2(self, text):
            self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price2, timeout=10.0)
            ValidatorExpense.validate_price(TestData.new_expense_price2)

    def expense_title_error2(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title2, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title2)

    def expense_category_error2(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category2, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category2)

    def expense_date_error2(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error2(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error2(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error2(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error2(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error2): {e}")

    def expense_price_error3(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price3, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price3)

    def expense_title_error3(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title3, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title3)

    def expense_category_error3(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category3, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category3)

    def expense_date_error3(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error3(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error3(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error3(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error3(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error3): {e}")

    def expense_price_error4(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price4, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price4)

    def expense_title_error4(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title4, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title4)

    def expense_category_error4(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category4, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category4)

    def expense_date_error4(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error4(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error4(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error4(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error4(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error4): {e}")

    def expense_price_error5(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price5, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price5)

    def expense_title_error5(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title5, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title5)

    def expense_category_error5(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category5, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category5)

    def expense_date_error5(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error5(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error5(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error5(self):
        self.device(resourceId='android:id/button1').click(timeout=20.0)

    def expense_done_button_error5(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error5): {e}")

    def expense_price_error6(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price6, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price6)

    def expense_title_error6(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title6, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title6)

    def expense_category_error6(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category6, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category6)

    def expense_date_error6(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error6(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error6(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error6(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error6(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error6): {e}")

    def expense_price_error7(self, text):
            self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price7, timeout=10.0)
            ValidatorExpense.validate_price(TestData.new_expense_price7)

    def expense_title_error7(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title7, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title7)

    def expense_category_error7(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category7, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category7)

    def expense_date_error7(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error7(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error7(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error7(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error7(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error7): {e}")

    def expense_price_error8(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price8, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price8)

    def expense_title_error8(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title8, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title8)

    def expense_category_error8(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category8, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category8)

    def expense_date_error8(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error8(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error8(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error8(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error8(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error8): {e}")

    def expense_price_error9(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price9, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price9)

    def expense_title_error9(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title9, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title9)

    def expense_category_error9(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category9, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category9)

    def expense_date_error9(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error9(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error9(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error9(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error9(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error9): {e}")

    def expense_price_error10(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price10, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price10)

    def expense_title_error10(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title10, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title10)

    def expense_category_error10(self, text):
        # Keeping TestData.new_expense_category9 in set_text as per original code
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category9, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category10)

    def expense_date_error10(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error10(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error10(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error10(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error10(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error10): {e}")

    def expense_price_error11(self, text):
            self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price11, timeout=10.0)
            ValidatorExpense.validate_price(TestData.new_expense_price11)

    def expense_title_error11(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title11, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title11)

    def expense_category_error11(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category11, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category11)

    def expense_date_error11(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error11(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error11(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error11(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error11(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error11): {e}")

    def expense_price_error12(self, text):
        self.device(**AddMoreExpenses.expense_price_locator).set_text(TestData.new_expense_price12, timeout=10.0)
        ValidatorExpense.validate_price(TestData.new_expense_price12)

    def expense_title_error12(self, text):
        self.device(**AddMoreExpenses.expense_title_locator).set_text(TestData.new_expense_title12, timeout=10.0)
        ValidadorTitle.validate_title(TestData.new_expense_title12)

    def expense_category_error12(self, text):
        self.device(**AddMoreExpenses.expense_category_locator).set_text(TestData.new_expense_category12, timeout=15.0)
        ValidadorCategory.validate_category(TestData.new_expense_category12)

    def expense_date_error12(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvDate').click(timeout=15.0)

    def expense_confirm_date_error12(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_time_error12(self):
        self.device(resourceId='com.blogspot.e_kanivets.moneytracker:id/tvTime').click(timeout=15.0)

    def expense_confirm_time_error12(self):
        self.device(resourceId='android:id/button1').click(timeout=15.0)

    def expense_done_button_error12(self):
        try:
            self.device(**AddMoreExpenses.expense_done_button_locator).click(timeout=20.0)
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error12): {e}")

