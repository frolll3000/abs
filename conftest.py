import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@allure.step("Открыть и закрыть браузер после выполнения тестового сценария")
@pytest.fixture
def open_and_close_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
