from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestStellarBurgerPersonalArea:
    def test_transition_to_personal_area(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        mess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//p[text() = 'В этом разделе вы можете изменить свои персональные данные']"))).text

        assert mess == 'В этом разделе вы можете изменить свои персональные данные'

    def test_transition_to_constructor(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(By.XPATH, ".//p[text() = 'Конструктор']/parent::a").click()
        mess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER)).text

        assert mess == 'Соберите бургер'

    def test_transition_to_logo(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(By.XPATH, ".//header/nav[1]/div[1]/a").click()
        mess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER)).text

        assert mess == 'Соберите бургер'

    def test_logout(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(By.XPATH, ".//button[text() = 'Выход']").click()
        mess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//h2[text() = 'Вход']"))).text

        assert mess == 'Вход'
