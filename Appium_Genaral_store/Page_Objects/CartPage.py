from appium.webdriver.common.appiumby import AppiumBy
from Utilities.Base_class import BaseClass

class CartPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    price = (AppiumBy.ID,"com.androidsample.generalstore:id/productPrice")
    Total_price = (AppiumBy.ID,"com.androidsample.generalstore:id/totalAmountLbl")
    Check_box = (AppiumBy.CLASS_NAME,"android.widget.CheckBox")
    Checkout_btn = (AppiumBy.CLASS_NAME,"android.widget.Button")


    def GetPrice(self):
        return self.driver.find_element(*CartPage.price).text

    def Get_Total(self):
        return  self.driver.find_element(*CartPage.Total_price).text

    def click_Checkbox(self):
        return self.driver.find_element(*CartPage.Check_box).click()

    def Checkout_button(self):
        return self.driver.find_element(*CartPage.Checkout_btn).click()