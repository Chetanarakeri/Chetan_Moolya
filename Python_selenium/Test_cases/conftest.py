import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--ignore-certificate-errors')
        # driver = webdriver.Chrome(options=chrome_options)
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Edge":
        service_obj = Service()
        driver = webdriver.Edge(service=service_obj)
    driver.implicitly_wait(15)
    driver.get("https://www.ajio.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()