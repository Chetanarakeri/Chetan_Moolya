import time
from PageObjects.Homepage import Homepage
from utilities.Baseclass import Baseclass
from selenium import webdriver

class TestCase(Baseclass):

        def test_case(self):
# searching type of product
                log = self.getLogger()
                homepage = Homepage(self.driver)
                homepage.Search()
                log.info("Getting watches")
                homepage.SearchButton()
#selecting categories
                homepage.Gender()
                time.sleep(3)
                homepage.Brand_section()
                homepage.Brand_select()
                log.info("selecting product")
                checkoutpage1 = homepage.product_sel()
# Adding product to cart and place order
                checkoutpage1.Addcart()
                checkoutpage1.Gotocart()
                txt = checkoutpage1.Getting_text()
                log.info("Text shown on Final page: "+txt)
                checkoutpage1.Shiporder()
                time.sleep(2)
                self.driver.save_screenshot("ImageAjio.png")

                assert "PROCEED TO SHIPPING" in txt