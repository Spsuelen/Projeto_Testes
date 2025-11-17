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



    def tearDown(self):
        self.d.app_stop("com.blogspot.e_kanivets.moneytracker")


if __name__ == '__main__':
    unittest.main()