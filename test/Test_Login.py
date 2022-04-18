import unittest
import HtmlTestRunner
import time
import sys
from config import config as cfg
from pages.LoginPage import LoginPage
from utilities.Utilities import logger
from utilities.Utilities import drivers
sys.path.append("C:/Projects/WebAutomationFrameWork/test")


class LoginTest(unittest.TestCase):
    logs = logger.logs()
    baseURL = cfg.links_config["LOGIN"]
    username = cfg.login_accounts["USERNAME"]
    password = cfg.login_accounts["PASSWORD"]
    driver = drivers.chromeDriver

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickLogout()
        time.sleep(3)
        self.assertEqual("Account Logout", self.driver.title, "Webpage is not available")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Automation Done.....")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Projects"
                                                                  "\\WebAutomationFramework\\reports"))
