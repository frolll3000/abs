import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from allure_commons.types import AttachmentType


@allure.step("Открыть страницу {page}")
def open_page(driver, page):
    driver.get(page)


@allure.step("Кликнуть на элемент {element_name}")
def click_element(driver, element, element_name=None):
    WebDriverWait(driver, constants.TIMEOUT).until(EC.visibility_of_element_located(element))
    driver.find_element(*element).click()


@allure.step("Сделать скриншот")
def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
