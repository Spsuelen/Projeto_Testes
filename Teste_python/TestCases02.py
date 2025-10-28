import os
import unittest
from datetime import date
from datetime import datetime
import time
from datetime import timedelta
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Data import TestData
from Reports import Reports
from AddExpensesPage import AddExpensesPage
from EditExpense import EditExpense
from ExclusionExpense import ExclusionExpense
from ReportsSelector import ExpenseListPage
from AddMoreExpenses import AddMoreExpenses
from ReportsSumary import ReportsSumary
from ValidadorCategory import ValidadorCategory
from ValidadorTitle import ValidadorTitle
from ValidatorExpense import ValidatorExpense
from Nav import Navigation


class test_TestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Pixel 2 API 30",
            "appPackage": "com.blogspot.e_kanivets.moneytracker",
            "appActivity": "com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity",
            "automationName": "uiautomator2",
            "autoGrantPermissions": True,
            "adbExecTimeout": 900000,
            "uiautomator2ServerInstallTimeout": 900000
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
        #self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)

        self.add_expenses_page = AddExpensesPage(self.driver)
        self.edit_expense = EditExpense(self.driver)
        self.exclusion_expense = ExclusionExpense(self.driver)
        self.reports_selector = ExpenseListPage(self.driver)
        self.add_more_expenses = AddMoreExpenses(self.driver)
        self.reports_sumary = ReportsSumary(self.driver)
        self.reports = Reports(self.driver)
        self.ValidadorCategory = ValidadorCategory()
        self.ValidadorTitle = ValidadorTitle()
        self.ValidatorExpense = ValidatorExpense()
        self.navigation = Navigation(self.driver)

    def test_navigate_to_results(self):
        time.sleep(2)
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.navigation.expenses_navigation))

        self.navigation.list_to_navigation()

        wait.until(EC.visibility_of_element_located(self.navigation.expenses_results))

        self.navigation.list_to_results()

        wait.until(EC.visibility_of_element_located(self.navigation.list_nav_summary))

        self.navigation.list_expenses_summary()

        wait.until(EC.visibility_of_element_located(self.navigation.list_nav_graph))

        self.navigation.list_expenses_graph()

        time.sleep(5)

        self.assertEqual("Results",
                         self.driver.find_element(By.XPATH,
                                                  '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                                                  '//android.widget.TextView[contains(@text, "Results")]').
                         get_attribute(
                             'text'))

    def tearDown(self):
        # Teardown
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()