from Basepage import BasePage

import time

loc = {
	"loginicon": "/html[1]/body[1]/div[1]/main[1]/header[1]/div[2]/nav[1]/ul[1]/div[1]/button[1]",
	"email": "//input[@id='emailInput']",
	"password": "//input[@id='passwordInput']",
	"login_button": "//button[@id='submitButton']",
	"accname": "//ul[@class='app-components-menus-HorizontalMenu-styles__list']//span[@class='sc-iAyFgw eGPYzx'][contains(text(),'S')]",
	"arrowoption": "//div[@class='sc-cvbbAY hiQMyw']//*[@class='sc-jAaTju hmBdsO']",
	"accsettings": "//a[@class='button button--secondary button--block'][contains(text(),'Account Settings')]",
	"checkemail": "//input[@type='email']",
	"searchtab": "//span[@class='search-text']",
	"searchbar": "//input[@id='search-input']",
	"festival": "//h3[@class='sc-VigVT fjhisk']",
	"festival_name": "//h1[text()='{}']",
	"festival_from_search": "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[1]/div[2]/h3[1]",
	"menu_button": "//button[@class='festicket-profile-menu-button']",
	"logout_button": "//a[@class='festicket-profile-menu-link festicket-profile-menu-logout']",
}


url = "https://www.festicket.com/"


class LoginPage(BasePage):

	def __init__(self,driver):
		self.driver=driver

	def load_page(self):
		self.driver.get(url)
		time.sleep(3)

	def login(self, data):
		self.press(loc["loginicon"])
		self.wait_for_element(loc["email"])
		self.type(loc["email"], data['email'])
		self.type(loc["password"], data['password'])
		self.press(loc["login_button"])
		self.wait_for_element(loc["accname"], timeout=10)
		time.sleep(3)
		assert self.is_element_visible(loc['accname'])

	def check_if_correct_account(self, data_email):
		self.press(loc['accname'])
		self.wait_for_element(loc["arrowoption"])
		self.press(loc["arrowoption"])
		self.wait_for_element(loc["accsettings"])
		self.press(loc["accsettings"])
		time.sleep(3)
		email = str(self.driver.find_element_by_xpath(loc["checkemail"]).get_attribute('value'))
		print "Logged in as correct user"
		assert data_email == email

	def search_and_find_festival(self, festival):
		self.press(loc["searchtab"])
		self.wait_for_element(loc["searchbar"])
		self.type_and_enter(loc["searchbar"], festival)
		time.sleep(5)
		self.press(loc["festival_from_search"])
		self.wait_for_element(loc["festival_name"].format(festival))
		festival_from_ui = (self.driver.find_element_by_xpath(loc["festival_name"].format(festival))).text
		print "Festival is same as searched for"
		assert str(festival_from_ui) == festival

	def logout(self):
		print "logging out"
		self.press(loc["menu_button"])
		self.wait_for_element(loc["logout_button"])
		self.press(loc["logout_button"])
		self.wait_for_element(loc["loginicon"])
		assert self.is_element_visible(loc["loginicon"])
		print "logged out succesfully"









