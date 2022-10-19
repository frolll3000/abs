from selenium.webdriver.common.by import By


class Calculation(object):
    BUTTON_CONTINUE = (By.XPATH, '//button[@name="calculate"]')
    CHECK_BOX_AGREEMENT = (By.XPATH, '//*[contains(text(), "Подтверждаю")]/span')


class DataInput(object):
    INPUT_FULL_NAME_INSURER = (By.XPATH, '//*[text()="ФИО страхователя:"]/following::input[@name="name"]')
    INPUT_DATE_BIRTH = (By.XPATH, '//input[@id="dateBirth"]')
    INPUT_PASSPORT_NUMBER = (By.XPATH, '//input[@id="id"]')
    INPUT_PASSPORT_DATE = (By.XPATH, '//input[@id="idDate"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@id="address"]')
    INPUT_PHONE = (By.XPATH, '//input[@id="phone"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
