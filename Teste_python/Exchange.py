from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Exchange(BasePage):

    expenses_navigation = (By.XPATH,'//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    expenses_exchange = (By.XPATH, '//android.widget.CheckedTextView[@resource-id='
                                   '"com.blogspot.e_kanivets.moneytracker:'
                                   'id/design_menu_item_text" and @text="Exchange rates"]')

    expenses_btn = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btn_add_exchange_rate')

    expenses_add = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')


    def list_to_navigation(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_navigation = wait.until(EC.element_to_be_clickable(self.expenses_navigation))
        list_expenses_navigation.click()

    def list_to_exchange(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_exchange = wait.until(EC.element_to_be_clickable(self.expenses_exchange))
        list_expenses_exchange.click()

    def list_to_btn_exchange(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn = wait.until(EC.element_to_be_clickable(self.expenses_btn))
        list_expenses_btn.click()

    def list_to_btn_add(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_add = wait.until(EC.element_to_be_clickable(self.expenses_add))
        list_expenses_add.click()

