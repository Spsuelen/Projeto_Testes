from datetime import date
from datetime import datetime
import time
from datetime import timedelta


class TestData(object):

    expense_price = "800"
    expense_price2 = "1800.00"
    expense_price3 = "25.5"
    expense_price4 = "350.1236"
    expense_price5 = ".1000"
    new_expense_price1 = "-5000"
    new_expense_price2 = "0"
    new_expense_price3 = "12.45"
    new_expense_price4 = "800.123"
    new_expense_price5 = "1"
    new_expense_price6 = ".0123"

    new_expense_price7 = "12."
    new_expense_price8 = "0012.45"
    new_expense_price9 = "1234706985"
    new_expense_price10 = "0.00"
    new_expense_price11 = "-800.12"
    new_expense_price12 = "0123456"

    expense_title = "Aluguel"
    expense_title2 = "Alimentacao da  dieta "
    expense_title3 = "$Creche"
    expense_title4 = "Aluguel roupa de formatura"
    expense_title5 = "1Financiamento "
    new_expense_title1 = "titulo123"
    new_expense_title2 = "passeios!"
    new_expense_title3 = "TituloMuitoLongoParaTestar"
    new_expense_title4 = "Tittulooaa"
    new_expense_title5 = "Titulo123"
    new_expense_title6 = "     "

    new_expense_title7 = "a"
    new_expense_title8 = "ab"
    new_expense_title9 = "aaabbb"
    new_expense_title10 = "12345"
    new_expense_title11 = "  "
    new_expense_title12 = "x"

    expense_category = "contas"
    expense_category2 = "frut@s"
    expense_category3 = "123Educacao"
    expense_category4 = "Moradia!"
    expense_category5 = "Locomocao"
    new_expense_category1 = "algoaleatorioparaotesteverificaraadiçãonoaplicativodevaloresincorretos"
    new_expense_category2 = "ab"
    new_expense_category3 = "abc   def"
    new_expense_category4 = "@2023#"
    new_expense_category5 = "teste!!!"
    new_expense_category6 = ".."

    new_expense_category7 = "a"
    new_expense_category8 = "aaabbb"
    new_expense_category9 = "categoria123"
    new_expense_category10 = "abc#def"
    new_expense_category11 = "abc def"
    new_expense_category12 = "abc@"

    expense_new_price = "1500"

    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M')
