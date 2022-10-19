import time
from selenium.webdriver.support.wait import WebDriverWait
import allure
import constants
import function
from locators import Calculation, DataInput
from selenium.webdriver.support import expected_conditions as EC
import fake_data


def test_button_continue_disable_without_accept_agreements(open_and_close_browser):
    """
    Шаг Расчет. Кнопка Продолжить недоступна без заполнения чекбокса соглашения.
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


@allure.issue("link to issue")
def test_switch_step_calculation_to_data_input_scroll_bottom(open_and_close_browser):
    """
    При переходе с шага Расчет на шаг Ввод данных скрол уходит в низ страницы.
    P.S. в тесте указан пример использования обозначения шагов при переиспользовании функций"
    """
    driver = open_and_close_browser
    function.open_page(driver, constants.PAGE_VIRUS_PROTECTION)
    function.click_element(driver, Calculation.CHECK_BOX_AGREEMENT, "чекбокс подтверждения отсутствия контакта зараженных лиц")
    function.click_element(driver, Calculation.BUTTON_CONTINUE, "кнопка Продолжить")
    function.take_screenshot(driver)
    with allure.step("Фокус страницы находится в верху"):
        assert driver.execute_script("return window.pageYOffset;") == 0


def test_aa(open_and_close_browser):
    driver = open_and_close_browser
    driver.get(constants.PAGE_VIRUS_PROTECTION)
    driver.find_element(*Calculation.CHECK_BOX_AGREEMENT).click()
    driver.find_element(*Calculation.BUTTON_CONTINUE).click()
    WebDriverWait(driver, constants.TIMEOUT).until(EC.visibility_of_element_located(DataInput.INPUT_FULL_NAME_INSURER))
    driver.find_element(*DataInput.INPUT_FULL_NAME_INSURER).send_keys(fake_data.get_full_name())

    driver.find_element(*DataInput.INPUT_DATE_BIRTH).click()
    driver.find_element(*DataInput.INPUT_DATE_BIRTH).send_keys(fake_data.get_birth_day())

    driver.find_element(*DataInput.INPUT_PASSPORT_NUMBER).send_keys(fake_data.get_passport_number())

    driver.find_element(*DataInput.INPUT_PASSPORT_DATE).click()
    driver.find_element(*DataInput.INPUT_PASSPORT_DATE).send_keys(fake_data.get_birth_day())

    driver.find_element(*DataInput.INPUT_ADDRESS).send_keys(fake_data.get_address())

    driver.find_element(*DataInput.INPUT_PHONE).send_keys(fake_data.get_phone_number())

    driver.find_element(*DataInput.INPUT_EMAIL).send_keys(fake_data.get_email())

