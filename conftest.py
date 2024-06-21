import pytest
from selenium import webdriver

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.AUTH_BUTTON).click()
    return driver