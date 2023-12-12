import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
cap=dict (
    deviceName= 'chetan',
    platformName='Android',
    appPackage='com.androidsample.generalstore',
    appActivity='com.androidsample.generalstore.SplashActivity',
)
appium_server_url = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(cap))
time.sleep(5)

# selecting countries and entering name and gender selction
driver.find_element(By.ID, "android:id/text1").click()
i=1
while i>0:
    countries = driver.find_elements(By.XPATH,"//android.widget.TextView")
    for ele in countries:
        if ele.text == "Aruba":
            ele.click()
            i -=1
            break
    else:
        driver.swipe(535,2054,389,676,500)

driver.find_element(By.ID,"com.androidsample.generalstore:id/nameField").send_keys("chetan kumar")
driver.find_element(By.ID,"com.androidsample.generalstore:id/radioMale").click()
driver.find_element(By.ID,"com.androidsample.generalstore:id/btnLetsShop").click()
time.sleep(5)

#scrolling to product and adding to cart

product = 'Converse All Star'
i=1
while i>0:
    products = driver.find_elements(By.XPATH,"//android.widget.TextView")
    for ele in products:
        if ele.text == product :
            ele.click()
            time.sleep(3)
            driver.swipe(825, 2011, 990, 2007, 500)
            time.sleep(4)

            i -=1
            break
    else:
            driver.swipe(535,2054,389,676,500)

driver.find_element(By.ID,"com.androidsample.generalstore:id/appbar_btn_cart").click()
time.sleep(2)

#getting product price and bill amount

price = driver.find_element(By.ID,"com.androidsample.generalstore:id/productPrice").text
time.sleep(3)
print(price)
bill_amount = driver.find_element(By.ID,"com.androidsample.generalstore:id/totalAmountLbl").text
print(bill_amount)
time.sleep(3)
driver.find_element(By.CLASS_NAME,"android.widget.CheckBox").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
time.sleep(5)
# assert price == bill_amou