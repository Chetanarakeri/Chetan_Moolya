from Utilities.Base_class import BaseClass
import time
from Page_Objects.HomePage import HomePage

class TestOrder(BaseClass):
    def test_case(self):
        # Hompage actions - selecting countries and entering name and gender selction
        homepage = HomePage(self.driver)
        homepage.CountryDrop()
        homepage.CountrySelect()
        homepage.Username("chetan")
        homepage.Gender()
        productpage1 = homepage.Lets_shop()
        time.sleep(3)
        #scrolling to product and adding to cart
        cartpage1 = productpage1.ProductSelect()
        time.sleep(2)
        #getting product price and bill amount
        price = str(cartpage1.GetPrice())
        bill_amount = str(cartpage1.Get_Total())
        cartpage1.click_Checkbox()
        cartpage1.Checkout_button()
        assert price == bill_amount.replace(' ','')