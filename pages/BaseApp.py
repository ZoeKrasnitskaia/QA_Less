class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://web-test15.chat2desk.com/"

    def open(self, url=""):
        self.driver.get(f"{self.base_url}{url}")