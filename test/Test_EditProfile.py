import unittest
import HtmlTestRunner
import time
import sys
from config import config as cfg
from pages.EditProfile import EditProfile
from pages.LoginPage import LoginPage
from utilities.Utilities import logger
from utilities.Utilities import drivers
from selenium.webdriver.common.keys import Keys

sys.path.append("C:/Projects/WebAutomationFrameWork/test")


class LoginTest(unittest.TestCase):
    logs = logger.logs()
    baseURL = cfg.links_config["LOGIN"]
    username = cfg.login_accounts["USERNAME"]
    password = cfg.login_accounts["PASSWORD"]
    firstname = cfg.edit_account["FIRSTNAME"]
    lastname = cfg.edit_account["LASTNAME"]
    email = cfg.edit_account["EMAIL"]
    telephone = cfg.edit_account["TELEPHONE"]
    driver = drivers.chromeDriver

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_edit(self):
        lp = LoginPage(self.driver)
        ep = EditProfile(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        ep.clickSubmit1()
        ep.setFirstname(Keys.DELETE)
        ep.setFirstname(self.firstname)
        ep.setLastname(self.lastname)
        ep.setEmail(self.email)
        ep.setTelephone(self.telephone)
        ep.clickSubmit2()
        time.sleep(3)
        self.assertEqual("My Account", self.driver.title, "Webpage is not available")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Automation Done.....")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Projects"
                                                                  "\\WebAutomationFramework\\reports"))
