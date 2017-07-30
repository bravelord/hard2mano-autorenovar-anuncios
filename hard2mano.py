import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import sys

binary = FirefoxBinary('localizacion firefox')
profile = webdriver.FirefoxProfile()
path = "localizacion xpath geckodriver"

driver = webdriver.Firefox(executable_path=path,firefox_profile=profile,firefox_binary=binary)


subir_links = [ #links h2m
''
]

driver.get('https://www.hard2mano.com/index.php?app=core&module=global&section=login')
user = driver.find_element_by_id("ips_username")
user.send_keys("username")
pas = driver.find_element_by_id("ips_password")
pas.send_keys("password")
driver.find_element_by_xpath("(//input[@class='input_submit'])").click()
time.sleep(5)

for link in subir_links:
	driver.get(link)

	##hacemos click a subir este tema
	subir1 = driver.find_element_by_xpath('//*[@title="Sube este tema"]')
	subir1.click()

	#esperar 35
	time.sleep(35)