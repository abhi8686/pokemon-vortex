from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get('http://www.pokemon-vortex.com/login.php')
time.sleep(5)
username = driver.find_element_by_name("myusername")
username.send_keys("Enter ur username")
password = driver.find_element_by_name("mypassword")
password.send_keys("Enter ur password here")
submittag = driver.find_element_by_name("Submit")
submittag.submit()


s = driver.current_url
j=0
while(j<100):
	if "zeta" in s:
		driver.get('http://zeta.pokemon-vortex.com/battle.php?bid=381258')
	else:
		driver.get('http://theta.pokemon-vortex.com/battle.php?bid=381258')
	i=0
	while(i<6):
		b = driver.find_element_by_tag_name("form")
		b.submit()
		time.sleep(1)
		try:
			c = driver.find_elements_by_tag_name("form")
			a=c[1]
			a.submit()
			time.sleep(1)
		except:
			c = driver.find_element_by_tag_name("form")
			c.submit()

		try:
			c = driver.find_elements_by_tag_name("form")
			a=c[1]
			a.submit()
			time.sleep(1)
		except:
			c = driver.find_element_by_tag_name("form")
			c.submit()
		i=i+1
	j=j+1


