import unittest
import HtmlTestRunner
import time
import sys
from pages.RegisterPage import RegisterPage
from config import config as cfg
from utilities.Utilities import logger
from utilities.Utilities import drivers
sys.path.append("C:/Projects/WebAutomationFrameWork")


class LoginTest(unittest.TestCase):
    logs = logger.logs()
    baseURL = cfg.links_config["REGISTER"]
    firstname = cfg.register_accounts["FIRSTNAME"]
    lastname = cfg.register_accounts["LASTNAME"]
    telephone = cfg.register_accounts["TELEPHONE"]
    email = cfg.register_accounts["EMAIL"]
    password = cfg.register_accounts["PASSWORD"]
    password_confirm = cfg.register_accounts["PASSWORD CONFIRMATION"]
    driver = drivers.chromeDriver

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_register(self):
        rp = RegisterPage(self.driver)
        rp.setFirstname(self.firstname)
        rp.setLastname(self.lastname)
        rp.setTelephone(self.telephone)
        rp.setEmail(self.email)
        rp.setPassword(self.password)
        rp.setPasswordConfirm(self.password_confirm)
        rp.clickNewsletters()
        rp.clickPrivacypolicy()
        rp.clickSubmit()
        time.sleep(3)
        self.assertEqual("Your Account Has Been Created!", self.driver.title, "Webpage is not available")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Automation Done.....")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Projects\\WebAutomationFramework\\reports"))
