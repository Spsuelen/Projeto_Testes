from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Navigation(BasePage):

    expenses_navigation = (By.XPATH,'//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    expenses_results = (By.XPATH,'//android.widget.CheckedTextView[@resource-id='
                          '"com.blogspot.e_kanivets.moneytracker:id/'
                        'design_menu_item_text" and @text="Results"]')

    list_nav_summary = (By.XPATH, '//android.widget.TextView[@text="SUMMARY"]')


    list_nav_graph = (By.XPATH, '//android.widget.TextView[@text="GRAPH"]')

    def list_to_navigation(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_navigation = wait.until(EC.element_to_be_clickable(self.expenses_navigation))
        list_expenses_navigation.click()

    def list_to_results(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_results = wait.until(EC.element_to_be_clickable(self.expenses_results))
        list_expenses_results.click()

    def list_expenses_summary(self):
        wait = WebDriverWait(self.driver, 30)
        list_list_nav_summary = wait.until(EC.element_to_be_clickable(self.list_nav_summary))
        list_list_nav_summary.click()

    def list_expenses_graph(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_graph_locator = wait.until(EC.element_to_be_clickable(self.list_nav_graph))
        list_expenses_graph_locator.click()