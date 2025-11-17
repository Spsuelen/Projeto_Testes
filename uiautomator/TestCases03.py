import os
import unittest
from datetime import date
from datetime import datetime
from datetime import timedelta
import uiautomator2 as u2
import time

from Data import TestData
from AddExpensesPage import AddExpensesPage
from Reports import Reports
from EditExpense import EditExpense
from ExclusionExpense import ExclusionExpense
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
        self.reports = Reports(self.d)
        self.ValidadorCategory = ValidadorCategory()
        self.ValidadorTitle = ValidadorTitle()
        self.ValidatorExpense = ValidatorExpense()
        self.navigation = Navigation(self.d)
        self.exchange = Exchange(self.d)
        self.imports = Imports(self.d)
        self.exports = Exports(self.d)
        self.accounts = Accounts(self.d)



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




    def tearDown(self):
        self.d.app_stop("com.blogspot.e_kanivets.moneytracker")


if __name__ == '__main__':
    unittest.main()