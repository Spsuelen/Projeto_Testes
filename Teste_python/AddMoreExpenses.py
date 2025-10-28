from datetime import date
from datetime import datetime
import time
from datetime import timedelta
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage
from ValidatorExpense import ValidatorExpense
from ValidadorCategory import ValidadorCategory
from ValidadorTitle import ValidadorTitle
from Data import TestData


class AddMoreExpenses(BasePage):
    expense_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    expense_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    expense_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    expense_date_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvDate")
    expense_confirm_date_locator = (By.ID, 'android:id/button1')
    expense_time_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvTime")
    expense_confirm_time_locator = (By.ID, 'android:id/button1')
    expense_done_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')

    # Segunda adição de Informações


    def expense_price2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price)
        ValidatorExpense.validate_price(TestData.expense_price2)

    def expense_title2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title2)
        ValidadorTitle. validate_title(TestData.expense_title)
        ValidadorTitle.validate_title(TestData.expense_title2)


    def expense_category2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category2)
        ValidadorCategory. validate_category(TestData.expense_category2)

    def expense_date2(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time2(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Terceira adição de Informações


    def expense_price3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price3)
        ValidatorExpense.validate_price(TestData.expense_price3)

    def expense_title3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title3)
        ValidadorTitle.validate_title(TestData.expense_title3)

    def expense_category3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category3)
        ValidadorCategory.validate_category(TestData.expense_category3)

    def expense_date3(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time3(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Quarta adição de Informações


    def expense_price4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price4)
        ValidatorExpense.validate_price(TestData.expense_price4)

    def expense_title4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title4)
        ValidadorTitle.validate_title(TestData.expense_title4)

    def expense_category4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category4)
        ValidadorCategory.validate_category(TestData.expense_category4)

    def expense_date4(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time4(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(
            EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Quinta adição de Informações


    def expense_price5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price5)
        ValidatorExpense.validate_price(TestData.expense_price5)

    def expense_title5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title5)
        ValidadorTitle.validate_title(TestData.expense_title5)

    def expense_category5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category5)
        ValidadorCategory.validate_category(TestData.expense_category5)

    def expense_date5(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date5(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time5(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time5(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button5(self):
        wait = WebDriverWait(self.driver, 15)
        expense_done_button = wait.until(
            EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()



    # Adicionando Informações Incorretas



    def expense_price_error1(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.new_expense_price1)
        ValidatorExpense.validate_price(TestData.new_expense_price1)

    def expense_title_error1(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.new_expense_title1)
        ValidadorTitle.validate_title(TestData.new_expense_title1)

    def expense_category_error1(self, text):
        wait = WebDriverWait(self.driver, 15)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.new_expense_category1)
        ValidadorCategory.validate_category(TestData.new_expense_category1)

    def expense_date_error1(self):
        wait = WebDriverWait(self.driver, 15)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date_error1(self):
        wait = WebDriverWait(self.driver, 15)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time_error1(self):
        wait = WebDriverWait(self.driver, 15)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time_error1(self):
        wait = WebDriverWait(self.driver, 15)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button_error1(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error2(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price2)
            ValidatorExpense.validate_price(TestData.new_expense_price2)

    def expense_title_error2(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title2)
            ValidadorTitle.validate_title(TestData.new_expense_title2)

    def expense_category_error2(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category2)
            ValidadorCategory.validate_category(TestData.new_expense_category2)

    def expense_date_error2(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error2(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error2(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error2(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error2(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error3(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price3)
            ValidatorExpense.validate_price(TestData.new_expense_price3)

    def expense_title_error3(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title3)
            ValidadorTitle.validate_title(TestData.new_expense_title3)

    def expense_category_error3(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category3)
            ValidadorCategory.validate_category(TestData.new_expense_category3)

    def expense_date_error3(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error3(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error3(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error3(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error3(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error4(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price4)
            ValidatorExpense.validate_price(TestData.new_expense_price4)

    def expense_title_error4(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title4)
            ValidadorTitle.validate_title(TestData.new_expense_title4)

    def expense_category_error4(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category4)
            ValidadorCategory.validate_category(TestData.new_expense_category4)

    def expense_date_error4(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error4(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error4(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error4(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error4(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")

    def expense_price_error5(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price5)
            ValidatorExpense.validate_price(TestData.new_expense_price5)

    def expense_title_error5(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title5)
            ValidadorTitle.validate_title(TestData.new_expense_title5)

    def expense_category_error5(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category5)
            ValidadorCategory.validate_category(TestData.new_expense_category5)

    def expense_date_error5(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error5(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error5(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error5(self):
            wait = WebDriverWait(self.driver, 20)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error5(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")



    def expense_price_error6(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price6)
            ValidatorExpense.validate_price(TestData.new_expense_price6)

    def expense_title_error6(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title6)
            ValidadorTitle.validate_title(TestData.new_expense_title6)

    def expense_category_error6(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category6)
            ValidadorCategory.validate_category(TestData.new_expense_category6)


    def expense_date_error6(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error6(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error6(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error6(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error6(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error7(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price7)
            ValidatorExpense.validate_price(TestData.new_expense_price7)

    def expense_title_error7(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title7)
            ValidadorTitle.validate_title(TestData.new_expense_title7)

    def expense_category_error7(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category7)
            ValidadorCategory.validate_category(TestData.new_expense_category7)


    def expense_date_error7(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error7(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error7(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error7(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error7(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error8(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price8)
            ValidatorExpense.validate_price(TestData.new_expense_price8)

    def expense_title_error8(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title8)
            ValidadorTitle.validate_title(TestData.new_expense_title8)

    def expense_category_error8(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category8)
            ValidadorCategory.validate_category(TestData.new_expense_category8)


    def expense_date_error8(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error8(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error8(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error8(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error8(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")


    def expense_price_error9(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price9)
            ValidatorExpense.validate_price(TestData.new_expense_price9)

    def expense_title_error9(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title9)
            ValidadorTitle.validate_title(TestData.new_expense_title9)

    def expense_category_error9(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category9)
            ValidadorCategory.validate_category(TestData.new_expense_category9)


    def expense_date_error9(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error9(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error9(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error9(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error9(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")

    def expense_price_error10(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price10)
            ValidatorExpense.validate_price(TestData.new_expense_price10)

    def expense_title_error10(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title10)
            ValidadorTitle.validate_title(TestData.new_expense_title10)

    def expense_category_error10(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category9)
            ValidadorCategory.validate_category(TestData.new_expense_category10)


    def expense_date_error10(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error10(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error10(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error10(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error10(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")

    def expense_price_error11(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price11)
            ValidatorExpense.validate_price(TestData.new_expense_price11)

    def expense_title_error11(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title11)
            ValidadorTitle.validate_title(TestData.new_expense_title11)

    def expense_category_error11(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category11)
            ValidadorCategory.validate_category(TestData.new_expense_category11)


    def expense_date_error11(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error11(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error11(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error11(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error11(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")

    def expense_price_error12(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
            expense_price.send_keys(TestData.new_expense_price12)
            ValidatorExpense.validate_price(TestData.new_expense_price12)

    def expense_title_error12(self, text):
            wait = WebDriverWait(self.driver, 10)
            expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
            expense_title.send_keys(TestData.new_expense_title12)
            ValidadorTitle.validate_title(TestData.new_expense_title12)

    def expense_category_error12(self, text):
            wait = WebDriverWait(self.driver, 15)
            expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
            expense_category.send_keys(TestData.new_expense_category12)
            ValidadorCategory.validate_category(TestData.new_expense_category12)


    def expense_date_error12(self):
            wait = WebDriverWait(self.driver, 15)
            current_date = TestData.date
            expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
            expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
            expense_date_element.click()

    def expense_confirm_date_error12(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_time_error12(self):
            wait = WebDriverWait(self.driver, 15)
            current_time = datetime.now().strftime('%H:%M')
            expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
            expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
            expense_time_locator.click()

    def expense_confirm_time_error12(self):
            wait = WebDriverWait(self.driver, 15)
            expense_confirm_date_locator = (By.ID, 'android:id/button1')
            expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
            expense_confirm_date_locator.click()

    def expense_done_button_error12(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            expense_done_button = wait.until(
                EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
            expense_done_button.click()
        except Exception as e:
            print(f"[WARN] Não foi possível concluir o 'Done' (error1): {e}")