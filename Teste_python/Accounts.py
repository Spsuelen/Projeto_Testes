from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Accounts(BasePage):

    expenses_navigation = (By.XPATH,'//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    expenses_accounts = (By.XPATH, '//android.widget.CheckedTextView[@resource-id='
                                   '"com.blogspot.e_kanivets.moneytracker:'
                                   'id/design_menu_item_text" and @text="Accounts"]')

    expenses_btn_accounts = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btn_add_account')
    expenses_btn_add = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')


    def list_to_navigation(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_navigation = wait.until(EC.element_to_be_clickable(self.expenses_navigation))
        list_expenses_navigation.click()

    def list_to_accounts(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_accounts = wait.until(EC.element_to_be_clickable(self.expenses_accounts))
        list_expenses_accounts.click()

    def list_to_btn_accounts(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_accounts = wait.until(EC.element_to_be_clickable(self. expenses_btn_accounts))
        list_expenses_btn_accounts.click()

    def list_to_btn_add(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_add = wait.until(EC.element_to_be_clickable(self. expenses_btn_add))
        list_expenses_btn_add.click()






