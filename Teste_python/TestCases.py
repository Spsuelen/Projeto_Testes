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
from Exchange import Exchange
from Imports import Imports
from Exports import Exports
from Accounts import Accounts


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
        self.exchange = Exchange(self.driver)
        self.imports = Imports(self.driver)
        self.exports = Exports(self.driver)
        self.accounts = Accounts(self.driver)

    def test_expense(self):
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

        self.reports.navigate_to_list_page()

        wait = WebDriverWait(self.driver, 20)

        # Espera até que o elemento de preço do TestData.expense_price seja clicável
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               f"//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvTitle'"
                                               f" and @text='{TestData.expense_title}']"))).click()

        time.sleep(3)

        self.edit_expense.edit_specific_expense(TestData.expense_new_price)

        self.reports.navigate_to_list_page()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               f"//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvTitle'"
                                               f" and @text='{TestData.expense_title}']"))).click()

        time.sleep(2)

        # Espera até que o botão de exclusão esteja visível
        exclusion_expense = ExclusionExpense(self.driver)
        exclusion_expense.delete_expense()

        self.assertEqual("Short summary",
                         self.driver.find_element(By.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                  'android.widget.FrameLayout/'
                                                  'android.widget.LinearLayout/'
                                                  'android.widget.FrameLayout/'
                                                  'androidx.drawerlayout.widget.DrawerLayout/'
                                                  'android.view.ViewGroup/'
                                                  'android.widget.LinearLayout[2]/'
                                                  'androidx.recyclerview.widget.RecyclerView/'
                                                  'android.widget.FrameLayout[1]/'
                                                  'android.widget.FrameLayout/'
                                                  'android.widget.LinearLayout/'
                                                  'android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                                                  'android.widget.TextView[1]').text)

    def test_expense_more_add02(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price2(TestData.expense_price2)
        self.add_more_expenses.expense_title2(TestData.expense_title2)
        self.add_more_expenses.expense_category2(TestData.expense_category2)
        self.add_more_expenses.expense_date2()
        self.add_more_expenses.expense_confirm_date2()
        self.add_more_expenses.expense_time2()
        self.add_more_expenses.expense_confirm_time2()
        self.add_more_expenses.expense_done_button2()
        time.sleep(2)
        self.assertEqual("Add expense",
                     self.driver.find_element(By.XPATH,
                                              '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text)

    def test_expense_more_add03(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price3(TestData.expense_price3)
        self.add_more_expenses.expense_title3(TestData.expense_title3)
        self.add_more_expenses.expense_category3(TestData.expense_category3)
        self.add_more_expenses.expense_date3()
        self.add_more_expenses.expense_confirm_date3()
        self.add_more_expenses.expense_time3()
        self.add_more_expenses.expense_confirm_time3()
        self.add_more_expenses.expense_done_button3()
        time.sleep(2)
        self.assertEqual("Add expense",
                     self.driver.find_element(By.XPATH,
                                              '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text)

    def test_expense_more_add04(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price4(TestData.expense_price4)
        self.add_more_expenses.expense_title4(TestData.expense_title4)
        self.add_more_expenses.expense_category4(TestData.expense_category4)
        self.add_more_expenses.expense_date4()
        self.add_more_expenses.expense_confirm_date4()
        self.add_more_expenses.expense_time4()
        self.add_more_expenses.expense_confirm_time4()
        self.add_more_expenses.expense_done_button4()
        time.sleep(2)
        self.assertEqual("Add expense",
                     self.driver.find_element(By.XPATH,
                                              '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text)

    def test_expense_more_add05(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price5(TestData.expense_price5)
        self.add_more_expenses.expense_title5(TestData.expense_title5)
        self.add_more_expenses.expense_category5(TestData.expense_category5)
        self.add_more_expenses.expense_date5()
        self.add_more_expenses.expense_confirm_date5()
        self.add_more_expenses.expense_time5()
        self.add_more_expenses.expense_confirm_time5()
        self.add_more_expenses.expense_done_button5()
        self.assertEqual("Add expense",
                     self.driver.find_element(By.XPATH,
                                              '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text)

    def test_expense_more_add06(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error1(TestData.new_expense_price1)
        self.add_more_expenses.expense_title_error1(TestData.new_expense_title1)
        self.add_more_expenses.expense_category_error1(TestData.new_expense_category1)
        self.add_more_expenses.expense_date_error1()
        self.add_more_expenses.expense_confirm_date_error1()
        self.add_more_expenses.expense_time_error1()
        self.add_more_expenses.expense_confirm_time_error1()
        self.add_more_expenses.expense_done_button_error1()
        self.assertEqual("Add expense",
                         self.driver.find_element(By.XPATH,
                                                  '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text)

    def test_expense_more_add07(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error2(TestData.new_expense_price2)
        self.add_more_expenses.expense_title_error2(TestData.new_expense_title2)
        self.add_more_expenses.expense_category_error2(TestData.new_expense_category2)
        self.add_more_expenses.expense_date_error2()
        self.add_more_expenses.expense_confirm_date_error2()
        self.add_more_expenses.expense_time_error2()
        self.add_more_expenses.expense_confirm_time_error2()
        self.add_more_expenses.expense_done_button_error2()

        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add08(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error3(TestData.new_expense_price3)
        self.add_more_expenses.expense_title_error3(TestData.new_expense_title3)
        self.add_more_expenses.expense_category_error3(TestData.new_expense_category3)
        self.add_more_expenses.expense_date_error3()
        self.add_more_expenses.expense_confirm_date_error3()
        self.add_more_expenses.expense_time_error3()
        self.add_more_expenses.expense_confirm_time_error3()
        self.add_more_expenses.expense_done_button_error3()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add09(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error4(TestData.new_expense_price4)
        self.add_more_expenses.expense_title_error4(TestData.new_expense_title4)
        self.add_more_expenses.expense_category_error4(TestData.new_expense_category4)
        self.add_more_expenses.expense_date_error4()
        self.add_more_expenses.expense_confirm_date_error4()
        self.add_more_expenses.expense_time_error4()
        self.add_more_expenses.expense_confirm_time_error4()
        self.add_more_expenses.expense_done_button_error4()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add10(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error5(TestData.new_expense_price5)
        self.add_more_expenses.expense_title_error5(TestData.new_expense_title5)
        self.add_more_expenses.expense_category_error5(TestData.new_expense_category5)
        self.add_more_expenses.expense_date_error5()
        self.add_more_expenses.expense_confirm_date_error5()
        self.add_more_expenses.expense_time_error5()
        self.add_more_expenses.expense_confirm_time_error5()
        self.add_more_expenses.expense_done_button_error5()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add11(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error6(TestData.new_expense_price6)
        self.add_more_expenses.expense_title_error6(TestData.new_expense_title6)
        self.add_more_expenses.expense_category_error6(TestData.new_expense_category6)
        self.add_more_expenses.expense_date_error6()
        self.add_more_expenses.expense_confirm_date_error6()
        self.add_more_expenses.expense_time_error6()
        self.add_more_expenses.expense_confirm_time_error6()
        self.add_more_expenses.expense_done_button_error6()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add12(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error7(TestData.new_expense_price7)
        self.add_more_expenses.expense_title_error7(TestData.new_expense_title7)
        self.add_more_expenses.expense_category_error7(TestData.new_expense_category7)
        self.add_more_expenses.expense_date_error7()
        self.add_more_expenses.expense_confirm_date_error7()
        self.add_more_expenses.expense_time_error7()
        self.add_more_expenses.expense_confirm_time_error7()
        self.add_more_expenses.expense_done_button_error7()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add13(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error8(TestData.new_expense_price8)
        self.add_more_expenses.expense_title_error8(TestData.new_expense_title8)
        self.add_more_expenses.expense_category_error8(TestData.new_expense_category8)
        self.add_more_expenses.expense_date_error8()
        self.add_more_expenses.expense_confirm_date_error8()
        self.add_more_expenses.expense_time_error8()
        self.add_more_expenses.expense_confirm_time_error8()
        self.add_more_expenses.expense_done_button_error8()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add14(self):
        self.driver.implicitly_wait(5)
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error9(TestData.new_expense_price9)
        self.add_more_expenses.expense_title_error9(TestData.new_expense_title9)
        self.add_more_expenses.expense_category_error9(TestData.new_expense_category9)
        self.add_more_expenses.expense_date_error9()
        self.add_more_expenses.expense_confirm_date_error9()
        self.add_more_expenses.expense_time_error9()
        self.add_more_expenses.expense_confirm_time_error9()
        self.add_more_expenses.expense_done_button_error9()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add15(self):
        self.driver.implicitly_wait(5)
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error10(TestData.new_expense_price10)
        self.add_more_expenses.expense_title_error10(TestData.new_expense_title10)
        self.add_more_expenses.expense_category_error10(TestData.new_expense_category10)
        self.add_more_expenses.expense_date_error10()
        self.add_more_expenses.expense_confirm_date_error10()
        self.add_more_expenses.expense_time_error10()
        self.add_more_expenses.expense_confirm_time_error10()
        self.add_more_expenses.expense_done_button_error10()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add16(self):
        self.driver.implicitly_wait(5)
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error11(TestData.new_expense_price11)
        self.add_more_expenses.expense_title_error11(TestData.new_expense_title11)
        self.add_more_expenses.expense_category_error11(TestData.new_expense_category11)
        self.add_more_expenses.expense_date_error11()
        self.add_more_expenses.expense_confirm_date_error11()
        self.add_more_expenses.expense_time_error11()
        self.add_more_expenses.expense_confirm_time_error11()
        self.add_more_expenses.expense_done_button_error11()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_expense_more_add17(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error12(TestData.new_expense_price12)
        self.add_more_expenses.expense_title_error12(TestData.new_expense_title12)
        self.add_more_expenses.expense_category_error12(TestData.new_expense_category12)
        self.add_more_expenses.expense_date_error12()
        self.add_more_expenses.expense_confirm_date_error12()
        self.add_more_expenses.expense_time_error2()
        self.add_more_expenses.expense_confirm_time_error12()
        self.add_more_expenses.expense_done_button_error12()
        self.assertEqual("Add expense",self.driver.find_element(By.XPATH,
                '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').text
    )

    def test_navigate(self):
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

        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.visibility_of_element_located(self.reports_selector.list_expenses_button_locator))

        self.reports_selector.navigate_to_expense_list()

        wait.until(EC.visibility_of_element_located(self.reports_selector.day_time_option_locator))

        self.reports_selector.select_all_time_option()

        wait.until(EC.visibility_of_element_located(self.reports_sumary.list_expenses_sumary_locator))

        self.reports_sumary.list_expenses_sumary()

        time.sleep(10)

        self.assertEqual("Report",
                         self.driver.find_element(By.XPATH,
                                                  '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                                                  '//android.widget.TextView[contains(@text, "Report")]').
                         get_attribute(
                             'text'))

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

    def test_navigate_to_exchange(self):
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

        wait.until(EC.visibility_of_element_located(self.exchange.expenses_navigation))

        self.exchange.list_to_navigation()

        wait.until(EC.visibility_of_element_located(self.exchange.expenses_exchange))

        self.exchange.list_to_exchange()

        wait.until(EC.visibility_of_element_located(self.exchange.expenses_btn))

        self.exchange.list_to_btn_exchange()

        wait.until(EC.visibility_of_element_located(self.exchange.expenses_add))

        self.exchange.list_to_btn_add()

        time.sleep(5)

        self.assertEqual("",
                         self.driver.find_element(By.ID,
                                                  'com.blogspot.e_kanivets.moneytracker:id/action_done').
                         get_attribute('text'))

    def test_navigate_to_exchange_import(self):
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

        wait.until(EC.visibility_of_element_located(self.imports.expenses_navigation))

        self.imports.list_to_navigation()

        wait.until(EC.visibility_of_element_located(self.imports.expenses_imports))

        self.imports.list_to_import()

        wait.until(EC.visibility_of_element_located(self.imports.expenses_info))

        self.imports.list_to_info()

        wait.until(EC.visibility_of_element_located(self.imports.expenses_btn_ok))

        self.imports.list_to_btn_ok()

        wait.until(EC.visibility_of_element_located(self.imports.expenses_btn_import))

        self.imports.list_to_btn_import()

        time.sleep(5)

        self.assertEqual("Import/Export",
                         self.driver.find_element(By.XPATH,
                                                  '//android.widget.TextView[@text="Import/Export"]').get_attribute(
                             'text'))

    def test_navigate_to_exchange_exports(self):
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
        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.visibility_of_element_located(self.exports.expenses_navigation))

        self.exports.list_to_navigation()

        wait.until(EC.visibility_of_element_located(self.exports.expenses_exports))

        self.exports.list_to_exports()

        wait.until(EC.visibility_of_element_located(self.exports.expenses_info))

        self.exports.list_to_info()

        wait.until(EC.visibility_of_element_located(self.exports.expenses_btn_ok))

        self.exports.list_to_btn_ok()

        wait.until(EC.visibility_of_element_located(self.exports.expenses_btn_exports))

        self.exports.list_to_btn_exports()

        wait.until(EC.visibility_of_element_located(self.exports.expenses_btn_options))

        self.exports.list_to_options()

        time.sleep(10)

        self.assertEqual("Import/Export",
                         self.driver.find_element(By.XPATH,
                                                  '//android.widget.TextView[@text="Import/Export"]').get_attribute(
                             'text'))

    def test_navigate_to_accounts(self):
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
        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.visibility_of_element_located(self.accounts.expenses_navigation))

        self.accounts.list_to_navigation()

        wait.until(EC.visibility_of_element_located(self.accounts.expenses_accounts))

        self.accounts.list_to_accounts()

        wait.until(EC.visibility_of_element_located(self.accounts.expenses_btn_accounts))

        self.accounts.list_to_btn_accounts()

        wait.until(EC.visibility_of_element_located(self.accounts.expenses_btn_add))

        self.accounts.list_to_btn_add()


        time.sleep(10)

        self.assertEqual("",
                         self.driver.find_element(By.ID,
                                                  'com.blogspot.e_kanivets.moneytracker:id/action_done').
                         get_attribute('text'))



    def tearDown(self):
        # Teardown
      self.driver.quit()

if __name__ == '__main__':
    unittest.main()