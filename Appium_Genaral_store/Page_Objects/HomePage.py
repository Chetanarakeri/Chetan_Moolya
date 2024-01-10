from appium.webdriver.common.appiumby import AppiumBy
from Utilities.Base_class import BaseClass
from Page_Objects.ProductsPage import ProductPage
class HomePage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    Country_dropdown = (AppiumBy.ID, "android:id/text1")
    Country_names = (AppiumBy.XPATH,"//android.widget.TextView")
    User_name = (AppiumBy.ID,"com.androidsample.generalstore:id/nameField")
    Gender_select = (AppiumBy.ID,"com.androidsample.generalstore:id/radioMale")
    Shop_button = (AppiumBy.ID,"com.androidsample.generalstore:id/btnLetsShop")


    def CountryDrop(self):
        self.driver.find_element(*HomePage.Country_dropdown).click()

    def CountrySelect(self):
        i = 1
        while i > 0:
            countries = self.driver.find_elements(*HomePage.Country_names)
            for ele in countries:
                if ele.text == "Aruba":
                    country = ele
                    i -= 1
                    break
            else:
                self.swipe(535, 2054, 389, 676, 500)

        return country.click()

    def Username(self,username):
        return self.driver.find_element(*HomePage.User_name).send_keys(username)

    def Gender(self):
        return self.driver.find_element(*HomePage.Gender_select).click()

    def Lets_shop(self):
        self.driver.find_element(*HomePage.Shop_button).click()
        productpage = ProductPage(self.driver)
        return productpage
