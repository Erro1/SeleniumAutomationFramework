class LoginPage():
    username = '//*[@id="input-email"]'
    password = '//*[@id="input-password"]'
    login_button_xpath = '//*[@id="content"]/div/div[2]/div/form/input'
    logout_button_xpath = '//*[@id="column-right"]/div/a[13]'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

