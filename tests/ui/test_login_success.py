from pages.LoginPage import LoginPage
import os
import pytest

if not os.getenv("GH_USER") or not os.getenv("GH_PASS"):
    pytest.skip("Данные для логина не настроены")

@pytest.mark.ui
def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(os.getenv("GH_USER"), os.getenv("GH_PASS"))

    avatar, username_in_menu = login_page.login_success()
    assert avatar.is_displayed(), "Аватар не отображается"
    assert username_in_menu.is_displayed(), "Меню не отображаентся"

@pytest.mark.ui
def test_login_with_wrong_creds(driver):
    login_page = LoginPage(driver)
    login_page.open()
    wrong_login = 'pipi'
    wrong_password = 'Qwerty1!'
    login_page.login(wrong_login, wrong_password)
    error = login_page.get_error_message()
    assert error.is_displayed(), "Сообщение об ошибке не отображается"
