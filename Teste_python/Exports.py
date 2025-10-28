from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Exports(BasePage):

    expenses_navigation = (By.XPATH,'//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    expenses_exports = (By.XPATH, '//android.widget.CheckedTextView[@resource-id='
                                 '"com.blogspot.e_kanivets.moneytracker:'
                                 'id/design_menu_item_text" and @text="Import/Export"]')

    expenses_info = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/action_help')

    expenses_btn_ok = (By.ID, 'android:id/button1')

    expenses_btn_exports = (By.ID,'com.blogspot.e_kanivets.moneytracker:id/btn_export')

    expenses_btn_options = (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Google"]')

    def list_to_navigation(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_navigation = wait.until(EC.element_to_be_clickable(self.expenses_navigation))
        list_expenses_navigation.click()

    def list_to_exports(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_exports = wait.until(EC.element_to_be_clickable(self.expenses_exports))
        list_expenses_exports.click()

    def list_to_info(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_info = wait.until(EC.element_to_be_clickable(self.expenses_info))
        list_expenses_info.click()

    def list_to_btn_ok(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_ok = wait.until(EC.element_to_be_clickable(self.expenses_btn_ok))
        list_expenses_btn_ok.click()

    def list_to_btn_exports(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_exports = wait.until(EC.element_to_be_clickable(self.expenses_btn_exports))
        list_expenses_btn_exports.click()

    def list_to_options(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_btn_options = wait.until(EC.element_to_be_clickable(self.expenses_btn_options))
        list_expenses_btn_options.click()




