import pytest
import time
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="class")
def setup(request):
    global driver
    cap = dict(
        deviceName='chetan',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    appium_server_url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(10)
    # time.sleep(4)
    request.cls.driver = driver
    yield
    driver.close()

