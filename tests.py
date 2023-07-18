from pages.lenta_com import LentaPage
from time import sleep
import allure


@allure.title("Поиск в яндексе")
def test_lenta_main_page(browser):
    lenta_main_page = LentaPage(browser)
    lenta_main_page.go_to_site('https://lenta.com/')
    sleep(10)
    # with allure.step("Проверка логотипа"):
    #     lenta_main_page.checking_logo()