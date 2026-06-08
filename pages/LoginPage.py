from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Из файла BaseApp.py импортируем класс BasePage
from .BaseApp import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "login-email")
    PASSWORD_INPUT = (By.ID, "login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login-form button")

    def open(self):
        # Открывает страницу логина (например, /login)
        super().open()

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        login_button.click()

    def is_login_successful(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON).is_displayed()