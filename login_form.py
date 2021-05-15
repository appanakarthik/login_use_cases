# Requirements
# In the login form, we should have
# Name, (Text Box)
# Mobile number should have different country options  (Drop Down)
# Mobile number,  (Text Box)
# Email(option),  (Text Box)
# Password (at least 6 characters) (Text Box)

# Test cases
# Login in to the website
# Check whether we are able to see the link to click on signup
# Check whether when we click on signup link it is redirecting to create account page or not
# Check whether are we able to enter name under name section
# Check whether are we able to select different country options from the drop down menu
# Check whether are we able to enter the mobile number Under text box
# Check whether water mark is present inside the text box for mobile number
# Check whether we are able to enter email address under email text box
# Check whether water mark is present inside the text box for for password (at least 6 characters)
# Check whether text is present Under password text box(Passwords must be at least 6 characters.)
# Check whether we are able to click on continue button
# Check whether when we give less number of characters Under 6, box is getting hi lighted and validate the text colour is showing in red
# Enter an existing email and check whether we are getting a message, email has already been used. Please try other


from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

class amazon_login(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path=os.path.expanduser('~/chromedriver'))
        cls.browser.get("https://www.amazon.in")
        cls.browser.maximize_window()

    def setUp(self):
        browser = self.browser
        ac = ActionChains(browser)
        ac.move_to_element(browser.find_element(By.XPATH, "//div[@id='nav-tools']//*[contains(text(), 'Hello, Sign in')]")).perform()
        browser.find_element(By.XPATH, "//div[@id='nav-flyout-ya-newCust']/a[@class='nav-a']").click()


    def test_fill_login_form(self):

        """fill the login form and submit the login form and check whether it got submitted success or not """

        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@name='customerName']")\
            .send_keys("appana")
        select = Select(self.browser.find_element_by_name('countryCode'))
        select.select_by_visible_text(u'AD +376')
        options = select.options
        for i, val in enumerate(options):
            if "IN +91" in val.text:
                select.select_by_index(i)
                break
        time.sleep(5)
        self.browser.find_element(By.XPATH,
                                  "//div[@class='a-fixed-left-grid-col a-col-right']/input[@id='ap_phone_number']")\
            .send_keys('9959252526')
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-micro']/input[@name='secondaryLoginClaim']")\
            .send_keys('appanakarthik@gmail.com')
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").clear()
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").\
            send_keys('appana123')
        # Assert next is click on continue button to create an account, as this live website we cannot do,
        # but a trial application can asert by checking whether the user is getting created or not through api
        # call form the backend

    def test_validate_password(self):
        """Validate password is failing or not when we give less number of characters  """

        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@name='customerName']").send_keys(
            "appana")
        select = Select(self.browser.find_element_by_name('countryCode'))
        select.select_by_visible_text(u'AD +376')
        options = select.options
        for i, val in enumerate(options):
            if "IN +91" in val.text:
                select.select_by_index(i)
                break
        self.browser.find_element(By.XPATH, "//div[@class='a-fixed-left-grid-col a-col-right']/input[@id='ap_phone_number']")\
            .send_keys('9959123456')
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-micro']/input[@name='secondaryLoginClaim']")\
            .send_keys(
            'aaaaaa@gmail.com')
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").clear()
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").send_keys(
            'appa')
        self.browser.find_element(By.XPATH, "//span[@class='a-button-inner']/input[@id='continue']").click()
        self.assertTrue(self.browser.find_element(By.XPATH, "//div[@id='auth-password-invalid-password-alert']"),
                        "This test case is failing becuase of less number of characters in the password field")

  def test_valdiate_email(self):
      """Validate email id if it is an existing email then check whether it is throwing an error or not """
      self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@name='customerName']").send_keys(
          "appana")
      select = Select(self.browser.find_element_by_name('countryCode'))
      select.select_by_visible_text(u'AD +376')
      options = select.options
      for i, val in enumerate(options):
          if "IN +91" in val.text:
              select.select_by_index(i)
              break
      self.browser.find_element(By.XPATH,
                           "//div[@class='a-fixed-left-grid-col a-col-right']/input[@id='ap_phone_number']").send_keys(
          '9959123456')
      self.browser.find_element(By.XPATH,
                           "//div[@class='a-row a-spacing-micro']/input[@name='secondaryLoginClaim']").send_keys(
          'appanakarthik@gmail.com')
      self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").clear()
      self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").send_keys(
          'appana123')
      self.browser.find_element(By.XPATH, "//span[@class='a-button-inner']/input[@id='continue']").click()
      self.assertTrue(self.browser.find_element(By.XPATH, "//span[@class='a-list-item']").text, "text is not coming")


    def test_placeholder_available(self):
        self.assertTrue(self.browser.find_element(By.XPATH,
                             "//div[@class='a-row a-spacing-base']/input[@placeholder='At least 6 characters']"),
                        "placeholder is not present in password box")

    def test_without_email(self):
        self.browser.find_element(By.XPATH,
                                  "//div[@class='a-row a-spacing-base']/input[@name='customerName']").send_keys(
            "appana")
        select = Select(self.browser.find_element_by_name('countryCode'))
        select.select_by_visible_text(u'AD +376')
        options = select.options
        for i, val in enumerate(options):
            if "IN +91" in val.text:
                select.select_by_index(i)
                break
        self.browser.find_element(By.XPATH,
                                  "//div[@class='a-fixed-left-grid-col a-col-right']/input[@id='ap_phone_number']") \
            .send_keys('9959123456')
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").clear()
        self.browser.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']/input[@id='ap_password']").send_keys(
            'appa')
        self.browser.find_element(By.XPATH, "//span[@class='a-button-inner']/input[@id='continue']").click()
        self.assertTrue(self.browser.find_element(By.XPATH, "//div[@id='auth-password-invalid-password-alert']"),
                        "This test case is failing becuase of less number of characters in the password field")

    def test_valdiate_text_message(self):
        self.assertTrue(self.browser.find_element(By.XPATH,"//div[@class ='auth-require-fields-match-group']"
                                                           "/div[@ class ='a-row a-spacing-base']/div[1]"
                                                           "//div[@ class ='a-alert-content']"), "alert message is not "
                                                                                                 "displaying")

    def teardown(self):
      self.browser.get("https://www.amazon.in")
