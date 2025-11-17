import os
import unittest
from datetime import date
from datetime import datetime
from datetime import timedelta
import uiautomator2 as u2
import time

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
        self.d = u2.connect()
        self.d.app_start("com.blogspot.e_kanivets.moneytracker", stop=True, wait=True)
        time.sleep(2)

        self.add_expenses_page = AddExpensesPage(self.d)
        self.edit_expense = EditExpense(self.d)
        self.exclusion_expense = ExclusionExpense(self.d)
        self.reports_selector = ExpenseListPage(self.d)
        self.add_more_expenses = AddMoreExpenses(self.d)
        self.reports_sumary = ReportsSumary(self.d)
        self.reports = Reports(self.d)
        self.ValidadorCategory = ValidadorCategory()
        self.ValidadorTitle = ValidadorTitle()
        self.ValidatorExpense = ValidatorExpense()
        self.navigation = Navigation(self.d)
        self.exchange = Exchange(self.d)
        self.imports = Imports(self.d)
        self.exports = Exports(self.d)
        self.accounts = Accounts(self.d)

    def test_expense(self):
        self.reports.navigate()

        self.reports.click_add_expenses_button()

        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        expense_title_xpath = (
            f"//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvTitle'"
            f" and @text='{TestData.expense_title}']")

        self.d.xpath(expense_title_xpath).click(timeout=20.0)

        self.edit_expense.edit_specific_expense(TestData.expense_new_price)

        self.d.xpath(expense_title_xpath).click(timeout=20.0)

        self.exclusion_expense.delete_expense()

        self.assertEqual("Short summary",
                         self.d.xpath(
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
                             'android.widget.TextView[1]').get_text())

    def test_expense_more_add02(self):
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
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add03(self):
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
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add04(self):
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
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add05(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price5(TestData.expense_price5)
        self.add_more_expenses.expense_title5(TestData.expense_title5)
        self.add_more_expenses.expense_category5(TestData.expense_category5)
        self.add_more_expenses.expense_date5()
        self.add_more_expenses.expense_confirm_date5()
        self.add_more_expenses.expense_time5()
        self.add_more_expenses.expense_confirm_time5()
        self.add_more_expenses.expense_done_button5()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add06(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error1(TestData.new_expense_price1)
        self.add_more_expenses.expense_title_error1(TestData.new_expense_title1)
        self.add_more_expenses.expense_category_error1(TestData.new_expense_category1)
        self.add_more_expenses.expense_date_error1()
        self.add_more_expenses.expense_confirm_date_error1()
        self.add_more_expenses.expense_time_error1()
        self.add_more_expenses.expense_confirm_time_error1()
        self.add_more_expenses.expense_done_button_error1()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add07(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error2(TestData.new_expense_price2)
        self.add_more_expenses.expense_title_error2(TestData.new_expense_title2)
        self.add_more_expenses.expense_category_error2(TestData.new_expense_category2)
        self.add_more_expenses.expense_date_error2()
        self.add_more_expenses.expense_confirm_date_error2()
        self.add_more_expenses.expense_time_error2()
        self.add_more_expenses.expense_confirm_time_error2()
        self.add_more_expenses.expense_done_button_error2()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add08(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error3(TestData.new_expense_price3)
        self.add_more_expenses.expense_title_error3(TestData.new_expense_title3)
        self.add_more_expenses.expense_category_error3(TestData.new_expense_category3)
        self.add_more_expenses.expense_date_error3()
        self.add_more_expenses.expense_confirm_date_error3()
        self.add_more_expenses.expense_time_error3()
        self.add_more_expenses.expense_confirm_time_error3()
        self.add_more_expenses.expense_done_button_error3()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add09(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error4(TestData.new_expense_price4)
        self.add_more_expenses.expense_title_error4(TestData.new_expense_title4)
        self.add_more_expenses.expense_category_error4(TestData.new_expense_category4)
        self.add_more_expenses.expense_date_error4()
        self.add_more_expenses.expense_confirm_date_error4()
        self.add_more_expenses.expense_time_error4()
        self.add_more_expenses.expense_confirm_time_error4()
        self.add_more_expenses.expense_done_button_error4()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add10(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error5(TestData.new_expense_price5)
        self.add_more_expenses.expense_title_error5(TestData.new_expense_title5)
        self.add_more_expenses.expense_category_error5(TestData.new_expense_category5)
        self.add_more_expenses.expense_date_error5()
        self.add_more_expenses.expense_confirm_date_error5()
        self.add_more_expenses.expense_time_error5()
        self.add_more_expenses.expense_confirm_time_error5()
        self.add_more_expenses.expense_done_button_error5()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add11(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error6(TestData.new_expense_price6)
        self.add_more_expenses.expense_title_error6(TestData.new_expense_title6)
        self.add_more_expenses.expense_category_error6(TestData.new_expense_category6)
        self.add_more_expenses.expense_date_error6()
        self.add_more_expenses.expense_confirm_date_error6()
        self.add_more_expenses.expense_time_error6()
        self.add_more_expenses.expense_confirm_time_error6()
        self.add_more_expenses.expense_done_button_error6()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add12(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error7(TestData.new_expense_price7)
        self.add_more_expenses.expense_title_error7(TestData.new_expense_title7)
        self.add_more_expenses.expense_category_error7(TestData.new_expense_category7)
        self.add_more_expenses.expense_date_error7()
        self.add_more_expenses.expense_confirm_date_error7()
        self.add_more_expenses.expense_time_error7()
        self.add_more_expenses.expense_confirm_time_error7()
        self.add_more_expenses.expense_done_button_error7()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add13(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error8(TestData.new_expense_price8)
        self.add_more_expenses.expense_title_error8(TestData.new_expense_title8)
        self.add_more_expenses.expense_category_error8(TestData.new_expense_category8)
        self.add_more_expenses.expense_date_error8()
        self.add_more_expenses.expense_confirm_date_error8()
        self.add_more_expenses.expense_time_error8()
        self.add_more_expenses.expense_confirm_time_error8()
        self.add_more_expenses.expense_done_button_error8()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add14(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error9(TestData.new_expense_price9)
        self.add_more_expenses.expense_title_error9(TestData.new_expense_title9)
        self.add_more_expenses.expense_category_error9(TestData.new_expense_category9)
        self.add_more_expenses.expense_date_error9()
        self.add_more_expenses.expense_confirm_date_error9()
        self.add_more_expenses.expense_time_error9()
        self.add_more_expenses.expense_confirm_time_error9()
        self.add_more_expenses.expense_done_button_error9()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add15(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error10(TestData.new_expense_price10)
        self.add_more_expenses.expense_title_error10(TestData.new_expense_title10)
        self.add_more_expenses.expense_category_error10(TestData.new_expense_category10)
        self.add_more_expenses.expense_date_error10()
        self.add_more_expenses.expense_confirm_date_error10()
        self.add_more_expenses.expense_time_error10()
        self.add_more_expenses.expense_confirm_time_error10()
        self.add_more_expenses.expense_done_button_error10()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add16(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error11(TestData.new_expense_price11)
        self.add_more_expenses.expense_title_error11(TestData.new_expense_title11)
        self.add_more_expenses.expense_category_error11(TestData.new_expense_category11)
        self.add_more_expenses.expense_date_error11()
        self.add_more_expenses.expense_confirm_date_error11()
        self.add_more_expenses.expense_time_error11()
        self.add_more_expenses.expense_confirm_time_error11()
        self.add_more_expenses.expense_done_button_error11()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_expense_more_add17(self):
        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error12(TestData.new_expense_price12)
        self.add_more_expenses.expense_title_error12(TestData.new_expense_title12)
        self.add_more_expenses.expense_category_error12(TestData.new_expense_category12)
        self.add_more_expenses.expense_date_error12()
        self.add_more_expenses.expense_confirm_date_error12()
        self.add_more_expenses.expense_time_error12()
        self.add_more_expenses.expense_confirm_time_error12()
        self.add_more_expenses.expense_done_button_error12()
        time.sleep(2)
        self.assertEqual("Add expense",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]//android.widget.TextView').
                         get_text())

    def test_navigate(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        time.sleep(2)
        self.reports_selector.navigate_to_expense_list()

        time.sleep(2)
        self.reports_selector.select_all_time_option()

        time.sleep(2)
        self.reports_sumary.list_expenses_sumary()

        time.sleep(10)

        self.assertEqual("Report",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                             '//android.widget.TextView[contains(@text, "Report")]').
                         get_text())

    def test_navigate_to_results(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        time.sleep(2)
        self.navigation.list_to_navigation()

        time.sleep(2)
        self.navigation.list_to_results()

        time.sleep(2)
        self.navigation.list_expenses_summary()

        time.sleep(2)
        self.navigation.list_expenses_graph()

        time.sleep(5)

        self.assertEqual("Results",
                         self.d.xpath(
                             '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                             '//android.widget.TextView[contains(@text, "Results")]').
                         get_text())

    def test_navigate_to_exchange(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        time.sleep(2)
        self.exchange.list_to_navigation()

        time.sleep(2)
        self.exchange.list_to_exchange()

        time.sleep(2)
        self.exchange.list_to_btn_exchange()

        time.sleep(2)
        self.exchange.list_to_btn_add()

        time.sleep(5)

        time.sleep(15)

        self.assertEqual("",
                         self.d(
                             resourceId='com.blogspot.e_kanivets.moneytracker:id/action_done').
                         get_text() or "")

    def test_navigate_to_exchange_import(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        time.sleep(2)
        self.imports.list_to_navigation()

        time.sleep(2)
        self.imports.list_to_import()

        time.sleep(2)
        self.imports.list_to_info()

        time.sleep(2)
        self.imports.list_to_btn_ok()

        time.sleep(2)
        self.imports.list_to_btn_import()

        time.sleep(5)

        self.assertEqual("Import/Export",
                         self.d.xpath(
                             '//android.widget.TextView[@text="Import/Export"]').
                         get_text())

    def test_navigate_to_exchange_exports(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        self.d(**self.exports.expenses_navigation).wait(timeout=15.0)
        self.exports.list_to_navigation()

        self.d.xpath(self.exports.expenses_exports.get('xpath')).wait(timeout=15.0)
        self.exports.list_to_exports()

        self.d(**self.exports.expenses_info).wait(timeout=15.0)
        self.exports.list_to_info()

        self.d(**self.exports.expenses_btn_ok).wait(timeout=15.0)
        self.exports.list_to_btn_ok()

        self.d(**self.exports.expenses_btn_exports).wait(timeout=15.0)
        self.exports.list_to_btn_exports()

        self.d(**self.exports.expenses_btn_options).wait(timeout=15.0)
        self.exports.list_to_options()

        time.sleep(10)

        self.assertEqual("Welcome to Gmail",
                         self.d.xpath(
                             '//android.widget.TextView[@text="Welcome to Gmail"]').get_text())

    def test_navigate_to_accounts(self):
        time.sleep(2)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        time.sleep(2)
        self.accounts.list_to_navigation()

        time.sleep(2)
        self.accounts.list_to_accounts()

        time.sleep(2)
        self.accounts.list_to_btn_accounts()

        time.sleep(2)
        self.accounts.list_to_btn_add()

        time.sleep(2)

        time.sleep(15)

        self.assertEqual("",
                         self.d(
                             resourceId='com.blogspot.e_kanivets.moneytracker:id/action_done').
                         get_text() or "")

    def tearDown(self):
        self.d.app_stop("com.blogspot.e_kanivets.moneytracker")


if __name__ == '__main__':
    unittest.main()