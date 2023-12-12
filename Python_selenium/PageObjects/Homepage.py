from selenium.webdriver.common.by import By
from PageObjects.Checkoutpage import Checkoutpage

class Homepage:
    def __init__(self,driver):
        self.driver = driver
# Locators
    seacrh_val = (By.XPATH,"//input[@name='searchVal']")
    search_btn = (By.CSS_SELECTOR,".ic-search")
    Gender_checkbox= (By.XPATH,"//label[@class='facet-linkname facet-linkname-genderfilter facet-linkname-Men']")
    brand_sec = (By.XPATH,"//span[@aria-label='brands']")
    brand_sel=(By.XPATH,"//label[@class='facet-linkname facet-linkname-brand facet-linkname-Adidas Originals']")
    prod_sel = (By.XPATH,"//div[@class='ReactVirtualized__Grid__innerScrollContainer']/div")

    def Search(self):
        return self.driver.find_element(*Homepage.seacrh_val).send_keys("watches")
    def SearchButton(self):
        return self.driver.find_element(*Homepage.search_btn).click()
    def Gender(self):
        return self.driver.find_element(*Homepage.Gender_checkbox).click()

    def Brand_section(self):
        return self.driver.find_element(*Homepage.brand_sec).click()

    def Brand_select(self):
        return self.driver.find_element(*Homepage.brand_sel).click()

    def product_sel(self):
        self.driver.find_element(*Homepage.prod_sel).click()
        checkoutpage = Checkoutpage(self.driver)
        return checkoutpage
