class Order():
    Item = '//a[text()="HP LP3065"]'
    AddtoCart = '//button[@id="button-cart"]'
    ButtonCart = 'cart-total'
    Checkout = '//p[@class="text-right"]/a[2]'

    def __init__(self, driver):
        self.driver = driver

    def clickItem(self):
        self.driver.find_element_by_xpath(self.Item).click()

    def clickAddtoCart(self):
        self.driver.find_element_by_xpath(self.AddtoCart).click()

    def clickCart(self):
        self.driver.find_element_by_xpath(self.ButtonCart).click()

    def clickCheckout(self):
        self.driver.find_element_by_xpath(self.Checkout).click()


class Customer():
    customer = '//input[@value="guest"]'
    Submit1 = 'button-account'
    firstname = 'input-payment-firstname'
    lastname = 'input-payment-lastname'
    email = 'input-payment-email'
    telephone = 'input-payment-telephone'
    city = 'input-payment-city'
    postcode = 'input-payment-postcode'
    region = 'input-payment-zone'
    Submit2 = '//input[@id="button-guest"]'

    def __init__(self, driver):
        self.driver = driver

    def setCustomer(self, customer):
        self.driver.find_element_by_xpath(self.customer).send_keys(customer)

    def clickSubmit1(self):
        self.driver.find_element_by_xpath(self.Submit1).click()

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element_by_xpath(self.telephone).send_keys(telephone)

    def setCity(self, city):
        self.driver.find_element_by_xpath(self.city).send_keys(city)

    def setPostcode(self, postcode):
        self.driver.find_element_by_xpath(self.postcode).send_keys(postcode)

    def setRegion(self, region):
        self.driver.find_element_by_xpath(self.region).send_keys(region)

    def clickSubmit2(self):
        self.driver.find_element_by_xpath(self.Submit2).click()


class ShippingMethod():
    ShippingButton = '//input[@id="button-shipping-method"]'
    TermsAndConditions = '//input[@name="agree"]'
    PaymentButton = '//input[@id="button-payment-method"]'
    ConfirmOrder = 'button-confirm'
    Submit3 = '//*[@id="content"]/div/div/a'

    def __init__(self, driver):
        self.driver = driver

    def clickShippingButton(self):
        self.driver.find_element_by_xpath(self.ShippingButton).click()

    def clickTermsAndConditions(self, tad):
        self.driver.find_element_by_xpath(self.TermsAndConditions).sendkeys(tad)

    def clickPaymentButton(self):
        self.driver.find_element_by_xpath(self.PaymentButton).click()

    def clickConfirmOrder(self):
        self.driver.find_element_by_xpath(self.ConfirmOrder).click()
