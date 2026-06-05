import pytest
from tests.loops_practice import Practice

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