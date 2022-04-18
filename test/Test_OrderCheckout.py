import unittest
import HtmlTestRunner
import time
import sys
from pages.OrderCheckout import Order
from config import config as cfg
from utilities.Utilities import logger
from utilities.Utilities import drivers
sys.path.append("C:/Users/Butch/PycharmProjects/WebAutomationFramework")


class LoginTest(unittest.TestCase):
    logs = logger.logs()
    baseURL = cfg.links_config["PRODUCT"]
    customer = cfg.guest_accounts["CUSTOMER"]
    firstname = cfg.guest_accounts["FIRSTNAME"]
    lastname = cfg.guest_accounts["LASTNAME"]
    telephone = cfg.guest_accounts["TELEPHONE"]
    email = cfg.guest_accounts["EMAIL"]
    city = cfg.guest_accounts["CITY"]
    postcode = cfg.guest_accounts["POSTCODE"]
    region = cfg.guest_accounts["REGION"]
    termsAndconditions = cfg.guest_accounts ["TERMS AND CONDITION"]
    driver = drivers.chromeDriver

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_order(self):
        o = Order(self.driver)
        o.clickItem()
        o.clickAddtoCart()
        o.clickCart()
        time.sleep(5)
        o.clickCheckout()


    #def test_customer(self):
    #    c = Customer(self.driver)
    #    c.customer(self.customer)
    #    c.clickSubmit1()
    #    c.setFirstname(self.firstname)
    #    c.setLastname(self.lastname)
    #    c.setTelephone(self.telephone)
    #    c.setEmail(self.email)
    #    c.setCity(self.city)
    #    c.setPostcode(self.postcode)
    #    c.setRegion(self.region)
    #    c.clickSubmit2()
    #    time.sleep(3)

    #def test_ship(self):
    #    ts.clickShippingButton()
    #    ts.clickTermsAndConditions(self.termsAndconditions)
    #    ts.clickPaymentButton()
    #    ts.clickConfirmOrder()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Automation Done.....")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Butch\\PycharmProjects"
                                                                  "\\WebAutomationFramework\\reports"))
