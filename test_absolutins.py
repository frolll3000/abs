from locators import FuncCalculation, FuncDataInput
from fake_data import FakeLibrary
import allure


@allure.title("Шаг Расчет. Кнопка Продолжить недоступна без заполнения чекбокса соглашения")
def test_button_continue_disable_without_accept_agreements(browser):
    """
    P.S. в тесте указан пример использования обозначения шагов с помощью "with allure.step"
    """
    calculation_page = FuncCalculation(browser)
    calculation_page.go_to_virus_protection_page()
    with allure.step("Кнопка Продолжить не активна"):
        assert calculation_page.get_property_button_continue() is True
    calculation_page.click_on_the_check_box_agreement()
    with allure.step("Кнопка Продолжить не активна"):
        assert calculation_page.get_property_button_continue() is False


@allure.title("При переходе с шага Расчет на шаг Ввод данных скрол уходит в низ страницы")
@allure.issue("link to issue")
def test_switch_step_calculation_to_data_input_scroll_bottom(browser):
    """
    P.S. в тесте указан пример использования обозначения шагов при переиспользовании функций с явным указанием локатора"
    """
    calculation_page = FuncCalculation(browser)
    calculation_page.go_to_virus_protection_page()
    calculation_page.click_on_the_check_box_agreement()
    calculation_page.click_on_the_button_continue()
    with allure.step("Фокус страницы находится в верху"):
        assert browser.execute_script("return window.pageYOffset;") == 0


@allure.title("Заполнение данных страхователя и переход к оплате")
def test_filling_insurer_data_and_go_to_payment(browser):
    """
    Заполнение данных страхователя и переход к оплате. Переадресация на банковскую страницу оплаты.
    """
    data_input_page = FuncDataInput(browser)
    calculation_page = FuncCalculation(browser)
    data_input_page.go_to_virus_protection_page()
    calculation_page.click_on_the_check_box_agreement()
    data_input_page.take_screenshot()
    calculation_page.click_on_the_button_continue()
    fake_data = FakeLibrary()
    data_input_page.enter_input_full_name(fake_data.get_full_name())
    data_input_page.enter_input_date_birth(fake_data.get_birth_day())
    data_input_page.enter_input_passport_number(fake_data.get_passport_number())
    data_input_page.enter_input_passport_date(fake_data.get_birth_day())
    data_input_page.enter_input_address(fake_data.get_address())
    data_input_page.enter_input_phone_number(fake_data.get_phone_number())
    data_input_page.enter_input_email(fake_data.get_email())
    data_input_page.take_screenshot()
    data_input_page.click_on_the_button_go_to_payment()
    data_input_page.opened_payment_page()
