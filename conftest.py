import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import constants


@allure.step("Открыть и закрыть браузер после выполнения тестового сценария")
@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(constants.TIMEOUT)
    yield driver
    driver.quit()
