from .base_page import BasePage
from time import sleep
from locators.lenta_com import LentaMainPageLocators


class LentaPage(BasePage):

    def checking_logo(self):
        """Проверка логотипа лентс"""
        lenta_logo = self.browser.find_element(*LentaMainPageLocators.HEADERS_LOGO).click()
        assert self.is_element_present(*LentaMainPageLocators.HEADERS_LOGO), "Логотип отсутствует"