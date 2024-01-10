from appium.webdriver.common.appiumby import AppiumBy
from Utilities.Base_class import BaseClass
from Page_Objects.CartPage import CartPage
import time

class ProductPage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    products = (AppiumBy.XPATH,"//android.widget.TextView")
    Add_to_cart_btn = (AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")

    def ProductSelect(self):
        product = "Converse All Star"
        i = 1
        while i > 0:
            products1 = self.driver.find_elements(*ProductPage.products)
            for ele in products1:
                if ele.text == product:
                    ele.click()
                    time.sleep(3)
                    self.swipe(825, 2011, 990, 2007, 500)
                    time.sleep(3)
                    i -= 1
                    break
            else:
                self.swipe(535,2054,389,676,500)

        self.driver.find_element(*ProductPage.Add_to_cart_btn).click()
        # time.sleep(3)
        cartpage = CartPage(self.driver)
        return cartpage




