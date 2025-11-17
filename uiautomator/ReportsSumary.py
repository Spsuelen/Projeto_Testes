import uiautomator2 as u2
from BasePage import BasePage


class ReportsSumary(BasePage):
    expenses_reports = {'resourceId': 'com.blogspot.e_kanivets.moneytracker:id/recyclerView'}
    list_expenses_sumary_locator = {'xpath': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                              'android.widget.FrameLayout/'
                                              'android.widget.LinearLayout/'
                                              'android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/'
                                              'android.view.ViewGroup/'
                                              'android.widget.LinearLayout[2]/'
                                              'androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/'
                                              'android.widget.FrameLayout/'
                                              'android.widget.LinearLayout/'
                                              'android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                                              'android.widget.TextView[1]'}

    def navigate_to_list_page_selector(self):
        self.device(**self.expenses_reports).click(timeout=30.0)

    def list_expenses_sumary(self):
        xpath_selector = self.list_expenses_sumary_locator.get('xpath')
        self.device.xpath(xpath_selector).click(timeout=30.0)