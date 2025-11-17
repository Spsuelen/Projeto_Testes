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





    def tearDown(self):
        self.d.app_stop("com.blogspot.e_kanivets.moneytracker")


if __name__ == '__main__':
    unittest.main()