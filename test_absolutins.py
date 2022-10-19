import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
import function
from locators import Calculation, DataInput, Payment
import fake_data


@allure.title("Шаг Расчет. Кнопка Продолжить недоступна без заполнения чекбокса соглашения")
def test_button_continue_disable_without_accept_agreements(open_and_close_browser):
    """
    P.S. в тесте указан пример использования обозначения шагов с помощью "with allure.step"
    """
    driver = open_and_close_browser
    with allure.step(f"Открыть страницу {constants.PAGE_VIRUS_PROTECTION}"):
        driver.get(constants.PAGE_VIRUS_PROTECTION)

    with allure.step("Кнопка Продолжить не активна"):
        assert driver.find_element(*Calculation.BUTTON_CONTINUE).get_property('disabled') is True

    with allure.step("Активировать чекбокс подтверждения отсутствия контакта зараженных лиц"):
        driver.find_element(*Calculation.CHECK_BOX_AGREEMENT).click()

    with allure.step("Кнопка Продолжить активна"):
        assert driver.find_element(*Calculation.BUTTON_CONTINUE).get_property('disabled') is False


@allure.title("При переходе с шага Расчет на шаг Ввод данных скрол уходит в низ страницы")
@allure.issue("link to issue")
def test_switch_step_calculation_to_data_input_scroll_bottom(open_and_close_browser):
    """
    P.S. в тесте указан пример использования обозначения шагов при переиспользовании функций с явным указанием локатора"
    """
    driver = open_and_close_browser
    function.open_page(driver, constants.PAGE_VIRUS_PROTECTION)
    function.click_element(driver, Calculation.CHECK_BOX_AGREEMENT, "Чекбокс подтверждения отсутствия контакта зараженных лиц")
    function.click_element(driver, Calculation.BUTTON_CONTINUE, "Кнопка Продолжить")
    with allure.step("Фокус страницы находится в верху"):
        assert driver.execute_script("return window.pageYOffset;") == 0


@allure.title("Заполнение данных страхователя и переход к оплате")
def test_filling_insurer_data_and_go_to_payment(open_and_close_browser):
    """
    Заполнение данных страхователя и переход к оплате. Переадресация на банковскую страницу оплаты.
    """
    driver = open_and_close_browser
    function.open_page(driver, constants.PAGE_VIRUS_PROTECTION)
    function.click_element(driver, Calculation.CHECK_BOX_AGREEMENT, "Чекбокс подтверждения отсутствия контакта зараженных лиц")
    function.take_screenshot(driver)
    function.click_element(driver, Calculation.BUTTON_CONTINUE, "Кнопка Продолжить")

    function.input_text(driver, DataInput.INPUT_FULL_NAME_INSURER, fake_data.get_full_name(), "Поле ФИО страхователя")
    function.input_text(driver, DataInput.INPUT_DATE_BIRTH, fake_data.get_birth_day(),
                        "Поле Дата рождения страхователя",
                        True)
    function.input_text(driver, DataInput.INPUT_PASSPORT_NUMBER, fake_data.get_passport_number(),
                        "Поле Серия/номер паспорта страхователя")
    function.input_text(driver, DataInput.INPUT_PASSPORT_DATE, fake_data.get_birth_day(),
                        "Поле Дата рождения страхователя",
                        True)
    function.input_text(driver, DataInput.INPUT_ADDRESS, fake_data.get_address(), "Поле Адрес регистрации")
    function.input_text(driver, DataInput.INPUT_PHONE, fake_data.get_phone_number(), "Поле Телефон")
    function.input_text(driver, DataInput.INPUT_EMAIL, fake_data.get_email(), "Поле Email")
    function.take_screenshot(driver)
    function.click_element(driver, DataInput.BUTTON_GO_TO_PAYMENT, "Кнопка Перейти к оплате")
    with allure.step("Осуществлена переадресация на страницу оплаты"):
        WebDriverWait(driver, constants.TIMEOUT).until(EC.url_contains(constants.SECURE_PAYMENTS_TINKOFF))
