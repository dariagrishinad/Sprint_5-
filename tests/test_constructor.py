from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerConstructor:
    def test_constructor_sauces(self, driver):
        driver.find_element(By.XPATH, ".//span[text() = 'Соусы']/parent::div").click()
        sauce = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//ul[2]/a[1]/p"))).text

        assert sauce == 'Соус Spicy-X'

    def test_constructor_fillings(self, driver):
        driver.find_element(By.XPATH, ".//span[text() = 'Начинки']/parent::div").click()
        filling = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//ul[3]/a[1]/p"))).text

        assert filling == 'Мясо бессмертных моллюсков Protostomia'

    def test_constructor_buns(self, driver):
        driver.find_element(By.XPATH, ".//span[text() = 'Соусы']/parent::div").click()
        driver.find_element(By.XPATH, ".//span[text() = 'Булки']/parent::div").click()
        bun = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//ul[1]/a[1]/p"))).text

        assert bun == 'Флюоресцентная булка R2-D3'