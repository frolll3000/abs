import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from allure_commons.types import AttachmentType


class BaseFunc:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = constants.PAGE_VIRUS_PROTECTION

    @allure.step("Сделать скриншот")
    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.step(f"Открыть страницу {constants.PAGE_VIRUS_PROTECTION}")
    def go_to_virus_protection_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, constants.TIMEOUT).until(EC.presence_of_element_located(locator),
                                                                   message=f"Can't find element by locator {locator}")

    def url_contains(self, url):
        return WebDriverWait(self.driver, constants.TIMEOUT).until(EC.url_contains(url))
