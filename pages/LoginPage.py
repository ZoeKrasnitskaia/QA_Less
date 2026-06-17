import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BaseApp import BasePage


class LoginPage(BasePage):
    LOGIN_PATH = "login"
    USERNAME_INPUT = (By.XPATH, "//input[@id='login_field']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@value='Sign in']")
    AVATAR_IMG = (By.XPATH, "//img[@data-testid='github-avatar']")
    USERNAME_IN_MENU = (By.XPATH, f"//div[@title='{os.getenv('GH_USER')}']")
    LOGIN_ERROR = (By.XPATH, "//div[@class ='flash-container']")

    def open(self):
        self.driver.get(f"{self.base_url}{self.LOGIN_PATH}")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

        wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)

        wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def login_success(self):
        wait = WebDriverWait(self.driver, 10)
        avatar = wait.until(EC.visibility_of_element_located(self.AVATAR_IMG))
        avatar.click()
        username_in_menu = wait.until(
            EC.visibility_of_element_located(self.USERNAME_IN_MENU)
        )
        return avatar, username_in_menu

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        error = wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR))
        return error
