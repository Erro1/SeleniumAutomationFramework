class RegisterPage():

    firstname = '//*[@id="input-firstname"]'
    lastname = '//*[@id="input-lastname"]'
    telephone = '//*[@id="input-telephone"]'
    email = '//*[@id="input-email"]'
    password = '//*[@id="input-password"]'
    password_confirm = '//*[@id="input-confirm"]'
    newsletters = '//*[@id="content"]/form/fieldset[3]/div/div/label[1]'
    privacy_policy = '//*[@id="content"]/form/div/div/input[1]'
    submit = '//*[@id="content"]/form/div/div/input[2]'

    def __init__(self, driver):
        self.driver = driver

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element_by_xpath(self.telephone).send_keys(telephone)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def setPasswordConfirm(self, passwordconfirm):
        self.driver.find_element_by_xpath(self.password_confirm).send_keys(passwordconfirm)

    def clickNewsletters(self):
        self.driver.find_element_by_xpath(self.newsletters).click()

    def clickPrivacypolicy(self):
        self.driver.find_element_by_xpath(self.privacy_policy).click()

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.submit).click()

