from selenium.webdriver.common.by import By
class Checkoutpage:

    def __init__(self,driver):
        self.driver = driver
# Locators
    addtocart = (By.XPATH,"//div[@class='pdp-addtocart-button']")
    gotocart = (By.XPATH,"//a[@class='go-to-cart-btn ']")
    shipping = (By.XPATH,"//button[@aria-label='Proceed to shipping']")
    Text = (By.XPATH,"//button[@class='rilrtl-button button shipping-button']")
    def Addcart(self):
        win = self.driver.window_handles
        self.driver.switch_to.window(win[1])
        return self.driver.find_element(*Checkoutpage.addtocart).click()

    def Gotocart(self):
        return self.driver.find_element(*Checkoutpage.gotocart).click()

    def Shiporder(self):
        return self.driver.find_element(*Checkoutpage.shipping)

    def Getting_text(self):
        return self.driver.find_element(*Checkoutpage.Text).text




