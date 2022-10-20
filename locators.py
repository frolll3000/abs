import allure
from selenium.webdriver.common.by import By
import constants
from function import BaseFunc


class Calculation:
    BUTTON_CONTINUE = (By.XPATH, '//button[@name="calculate"]')
    CHECK_BOX_AGREEMENT = (By.XPATH, '//*[contains(text(), "Подтверждаю")]/span')


class DataInput:
    INPUT_FULL_NAME_INSURER = (By.XPATH, '//*[text()="ФИО страхователя:"]/following::input[@name="name"]')
    INPUT_DATE_BIRTH = (By.XPATH, '//input[@id="dateBirth"]')
    INPUT_PASSPORT_NUMBER = (By.XPATH, '//input[@id="id"]')
    INPUT_PASSPORT_DATE = (By.XPATH, '//input[@id="idDate"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@id="address"]')
    INPUT_PHONE = (By.XPATH, '//input[@id="phone"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    BUTTON_GO_TO_PAYMENT = (By.XPATH, '//button[text()="Перейти к оплате"]')


class FuncCalculation(BaseFunc):
    @allure.step("Кликнуть на чекбокс подтверждения отсутствия контакта зараженных лиц")
    def click_on_the_check_box_agreement(self):
        return self.find_element(Calculation.CHECK_BOX_AGREEMENT).click()

    @allure.step("Кликнуть на кнопку продолжить")
    def click_on_the_button_continue(self):
        return self.find_element(Calculation.BUTTON_CONTINUE).click()

    def get_property_button_continue(self):
        return self.find_element(Calculation.BUTTON_CONTINUE).get_property('disabled')


class FuncDataInput(BaseFunc):
    @allure.step("Заполнить поле ФИО страхователя значением: {text}")
    def enter_input_full_name(self, text):
        return self.find_element(DataInput.INPUT_FULL_NAME_INSURER).send_keys(text)

    @allure.step("Заполнить поле Дата рождения страхователя значением: {text}")
    def enter_input_date_birth(self, text):
        field_date_birth = self.find_element(DataInput.INPUT_DATE_BIRTH)
        field_date_birth.click()
        field_date_birth.send_keys(text)
        return field_date_birth

    @allure.step("Заполнить поле Серия/номер паспорта страхователя значением: {text}")
    def enter_input_passport_number(self, text):
        return self.find_element(DataInput.INPUT_PASSPORT_NUMBER).send_keys(text)

    @allure.step("Заполнить поле Дата выдачи значением: {text}")
    def enter_input_passport_date(self, text):
        field_passport_date = self.find_element(DataInput.INPUT_PASSPORT_DATE)
        field_passport_date.click()
        field_passport_date.send_keys(text)
        return field_passport_date

    @allure.step("Заполнить поле Адрес регистрации значением: {text}")
    def enter_input_address(self, text):
        return self.find_element(DataInput.INPUT_ADDRESS).send_keys(text)

    @allure.step("Заполнить поле Телефон значением: {text}")
    def enter_input_phone_number(self, text):
        return self.find_element(DataInput.INPUT_PHONE).send_keys(text)

    @allure.step("Заполнить поле Email значением: {text}")
    def enter_input_email(self, text):
        return self.find_element(DataInput.INPUT_EMAIL).send_keys(text)

    @allure.step("Кликнуть на кнопку Перейти к оплате")
    def click_on_the_button_go_to_payment(self):
        return self.find_element(DataInput.BUTTON_GO_TO_PAYMENT).click()

    @allure.step("Осуществлена переадресация на страницу оплаты")
    def opened_payment_page(self):
        return self.url_contains(constants.SECURE_PAYMENTS_TINKOFF)
