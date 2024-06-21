from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestStellarBurgerAuthorization:
    def test_authorization_with_button_login_to_account(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON)).text

        assert enter == "Оформить заказ"

    def test_authorization_with_button_personal_area(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON)).text

        assert enter == "Оформить заказ"

    def test_authorization_with_button_in_registration_form(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON)).text

        assert enter == "Оформить заказ"

    def test_authorization_with_button_in_password_recovery(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(By.XPATH, ".//a[text() = 'Восстановить пароль']").click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON)).text

        assert enter == "Оформить заказ"






