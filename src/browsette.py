from selenium import webdriver

class Browsette:

	def __init__(self, browser, version):
		if browser == 'chrome':
			self.driver = webdriver.Chrome(executable_path=r"drivers/chrome/"+version+"/chromedriver")
		elif browser == 'firefox':
			self.driver = webdriver.Firefox(executable_path=r'drivers/firefox/'+version+'/geckodriver')

	def __open_chrome__(self, version):
		pass

	def __open_firefox__(self, version):
		pass

	def set_resolution(self, w, h):
		self.driver.set_window_size(w, h)

	def goto(self, url):
		self.driver.get(url)

	def screenshot(self, path):
		self.driver.save_screenshot(path+".png")
