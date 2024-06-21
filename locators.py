from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    EMAIL_FOR_AUTHORIZATION = (By.XPATH, ".//fieldset[1]/div/div/input")  # Инпут с email для авторизации
    PASSWORD_FOR_AUTHORIZATION = (By.XPATH, ".//fieldset[2]/div/div/input")  # Инпут с паролем для авторизации
    AUTH_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти" в форме авторизации
    CHECK_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" для проверки авторизации
    LOGIN_LINK = (By.XPATH, ".//a[text() = 'Войти']")  # Ссылка "Войти" в формах регистрации и восстанавления пароля
    REGISTRATION_LINK = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")  # Ссылка "Зарегистироваться"
    NAME = (By.XPATH, ".//fieldset[1]/div/div/input")  # Инпут для ввода имени в форме регистрации
    EMAIL_FOR_REGISTRATION = (By.XPATH, ".//fieldset[2]/div/div/input")  # Инпут с email для регистрации
    PASSWORD_FOR_REGISTRATION = (By.XPATH, ".//fieldset[3]/div/div/input")  # Инпут с паролем для регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']/parent::a")
    COLLECT_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
