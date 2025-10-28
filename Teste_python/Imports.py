from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Imports(BasePage):

    expenses_navigation = (By.XPATH,'//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    expenses_imports = (By.XPATH, '//android.widget.CheckedTextView[@resource-id='
                                 '"com.blogspot.e_kanivets.moneytracker:'
                                 'id/design_menu_item_text" and @text="Import/Export"]')

    expenses_info = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/action_help')

    expenses_btn_ok = (By.ID, 'android:id/button1')

    expenses_btn_import = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btn_import')





    def list_to_navigation(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_navigation = wait.until(EC.element_to_be_clickable(self.expenses_navigation))
        list_expenses_navigation.click()

    def list_to_import(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_import = wait.until(EC.element_to_be_clickable(self.expenses_imports))
        list_expenses_import.click()

    def list_to_info(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_info = wait.until(EC.element_to_be_clickable(self.expenses_info))
        list_expenses_info.click()

    def list_to_btn_ok(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_ok = wait.until(EC.element_to_be_clickable(self.expenses_btn_ok))
        list_expenses_btn_ok.click()

    def list_to_btn_import(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_import = wait.until(EC.element_to_be_clickable(self.expenses_btn_import))
        list_expenses_btn_import.click()



