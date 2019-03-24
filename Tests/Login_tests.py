from Testdriver import TestDriver
from modules.Loginpage import LoginPage


data = {
	"email": "sujisudheer13@gmail.com",
	"password": "parrot$19",
}

festival = 'Tomorrowland 2019'


class LoginTests(TestDriver):

	# test to check if the page loads
	def test_01_loginpage(self):
		page = LoginPage(self.driver)
		page.load_page()

	# test to check logging into portal
	def test_02_login_into_portal(self):
		page = LoginPage(self.driver)
		page.login(data)

	# test to check if logged into correct account
	def test_03_check_if_logged_account_is_current_account(self):
		page = LoginPage(self.driver)
		page.check_if_correct_account(data['email'])

	# test to search festival
	def test_04_search_festival(self):
		page = LoginPage(self.driver)
		page.search_and_find_festival(festival)

	# test to logout
	def test_05_logout(self):
		page = LoginPage(self.driver)
		page.logout()

