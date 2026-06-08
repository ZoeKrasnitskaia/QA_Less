from pages.LoginPage import LoginPage


def test_login_success(driver):
    login_page = LoginPage(driver)

    # Шаг 1: Открываем страницу
    login_page.open()

    # Шаг 2: Выполняем логин с тестовыми данными
    login_page.login("correct_user", "correct_password")

    # Шаг 3: Проверка (pytest assert)
    assert login_page.is_login_successful() == True, "Вход не выполнен: приветственный элемент не найден"
