import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from allure_commons.types import AttachmentType


@allure.step("Открыть страницу {page}")
def open_page(driver, page):
    driver.get(page)


@allure.step("Кликнуть на элемент {element_name}")
def click_element(driver, locator, element_name=None):
    WebDriverWait(driver, constants.TIMEOUT).until(EC.visibility_of_element_located(locator))
    driver.find_element(*locator).click()


@allure.step("Сделать скриншот")
def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@allure.step("Ввести текст: {text} в {input_name}")
def input_text(driver, locator, text, input_name=None, click_before_input=False):
    if click_before_input:
        click_element(driver, locator)
    driver.find_element(*locator).send_keys(text)
