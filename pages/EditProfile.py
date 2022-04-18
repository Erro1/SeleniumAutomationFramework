class EditProfile():
    firstname = '//*[@id="input-firstname"]'
    lastname = '//*[@id="input-lastname"]'
    email = '//*[@id="input-email"]'
    telephone = '//*[@id="input-telephone"]'
    submit1 = '//*[@id="content"]/ul[1]/li[1]/a'
    submit2 = '//*[@id="content"]/form/div/div[2]/input'

    def __init__(self, driver):
        self.driver = driver

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname).clear()
        self.driver.find_element_by_xpath(self.firstname).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname).clear()
        self.driver.find_element_by_xpath(self.lastname).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.email).clear()
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element_by_xpath(self.telephone).clear()
        self.driver.find_element_by_xpath(self.telephone).send_keys(telephone)

    def clickSubmit1(self):
        self.driver.find_element_by_xpath(self.submit1).click()

    def clickSubmit2(self):
        self.driver.find_element_by_xpath(self.submit2).click()
