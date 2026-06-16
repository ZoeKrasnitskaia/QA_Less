import pytest
from pages.loops_practice import Practice
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def practice():
    print("\nСоздаём объект Practice")
    yield Practice()
    print("\nУдаляем объект Practice")

@pytest.fixture(autouse=True)
def setup():
    print("Подготовка окружения")
    yield
    print("Очистка окружения")

@pytest.fixture
def open_file():
    file = open("open_file.txt", "w")
    print ("File opened")
    yield file
    file.close()
    print("File closed")

@pytest.fixture
def driver():
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(10)
    # yield driver
    # driver.quit()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()