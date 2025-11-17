import uiautomator2 as u2
from BasePage import BasePage
import time


class Exports(BasePage):

    expenses_navigation = {'description': 'Open navigation drawer'}

    expenses_exports = {'xpath': '//android.widget.CheckedTextView[@resource-id='
                                 '"com.blogspot.e_kanivets.moneytracker:'
                                 'id/design_menu_item_text" and @text="Import/Export"]'}

    expenses_info = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/action_help'}

    expenses_btn_ok = {'resourceId': 'android:id/button1'}

    expenses_btn_exports = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/btn_export'}

    # LOCALIZADOR CORRETO PARA CLICAR NO ÍCONE DO GMAIL NA TELA DE COMPARTILHAMENTO
    # Se o texto for 'Gmail' (como na Captura 175655.png):
    expenses_btn_options = {'text': 'Gmail'}

    def list_to_navigation(self):
        self.device(**self.expenses_navigation).click(timeout=30.0)

    def list_to_exports(self):
        xpath_selector = self.expenses_exports.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)

    def list_to_info(self):
        self.device(**self.expenses_info).click(timeout=30.0)

    def list_to_btn_ok(self):
        self.device(**self.expenses_btn_ok).click(timeout=30.0)

    def list_to_btn_exports(self):
        self.device(**self.expenses_btn_exports).click(timeout=30.0)

    def list_to_options(self):
        # Clica na opção de compartilhamento (Gmail)
        self.device(**self.expenses_btn_options).click(timeout=50.0)