from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators

faker = Faker()


class TestStellarBurgerRegistration:
    def test_successful_registration(self, driver):
        name = Constants.NAME
        email = faker.email()
        password = Constants.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//h2[text() = 'Вход']"))).text

        assert enter == "Вход"

    def test_registration_with_invalid_password(self, driver):
        name = Constants.NAME
        email = faker.email()
        password = '12345'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text() = 'Некорректный пароль']"))).text

        assert enter == "Некорректный пароль"

