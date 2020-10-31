from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import smtplib
import datetime
import time

now = datetime.datetime.now()
finaldate = now.replace(month=10, day=18, hour=19, minute=0, second=0, microsecond=0)

def sendemail(from_addr, to_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

while (now < finaldate):

	now = datetime.datetime.now()

	option = webdriver.ChromeOptions()
	option.add_argument("--headless")
	option.add_argument("--incognito")

	browser = webdriver.Chrome(executable_path='/Users/jtuyen/Documents/Coding Projects/selenium/chromedriver', options=option)

	browser.get("https://www.eventbrite.com/e/a-discussion-with-jake-robertson-sponsored-by-maurten-nutrition-tickets-50869918295?aff=efbeventtix")

	timeout = 20

	try:
	    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='listing-hero-image js-picturefill-img listing-image--main']")))
	except TimeoutException:
	    print("Timed out waiting for page to load")
	    browser.quit()

	status_element = browser.find_elements_by_xpath("//div[@data-automation='micro-ticket-box-status']")

	status = [x.text for x in status_element]

	print('status:')
	print(status, '\n')

	browser.quit()

	if len(status) == 0:
		sendemail(from_addr    = 'y2yenk@gmail.com', 
	    	to_addr_list = ['john.tuyen@gmail.com'],
	        subject      = 'Eventbrite ticket available!', 
	        message      = 'Registration link - https://www.eventbrite.com/e/a-discussion-with-jake-robertson-sponsored-by-maurten-nutrition-tickets-50869918295', 
	        login        = 'x@gmail.com', 
	        password     = 'x')
		print('Available and email sent')
		break
	else:
		print('Not available - ', now)
		time.sleep(600) #10 minutes