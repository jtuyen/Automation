from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib

f = open("gmail.creds","r")
lines = f.readlines()
login = lines[0]
password = lines[1]
f.close()

def sendemail(from_addr, to_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='./chromedriver', options=option)

sportinglife = ["https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-beacon-v1-running-shoe-25050741_000_080.html",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-vongo-v3-running-shoe-25050675_000_080.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25057670_000_090.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-zoom-fly-running-shoe-25057134_000_090.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25057142_000_095.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25019084_000_080.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25057126_000_085.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25044546_000_100.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-epic-react-flyknit-running-shoe-25057118_000_085.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-freedom-iso-2-running-shoe-25049909_000_080.html?cgid=shoes-men-running-shoes",
"https://www.sportinglife.ca/en-CA/shoes/men/running-shoes/mens-freedom-iso-2-running-shoe-25049891_000_080.html?cgid=shoes-men-running-shoes"]
sportchek = ["https://www.sportchek.ca/categories/men/footwear/running-shoes/product/new-balance-mens-fresh-foam-beacon-v1-running-shoes-blueorange-332558978.html#332558978%5Bcolor%5D=40",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/neutral/product/nike-mens-zoom-winflo-5-run-shield-running-shoes-blacksilvergr-332625096.html#332625096%5Bcolor%5D=01",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/neutral/product/nike-mens-air-zoom-pegasus-35-shield-running-shoes-greensilver-332624313.html#332624313%5Bcolor%5D=30",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/neutral/product/nike-mens-air-zoom-pegasus-35-turbo-running-shoes-blueorangere-332624849.html#332624849%5Bcolor%5D=40",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/product/nike-mens-epic-react-flyknit-running-shoes-navybluegrey-332619899.html#332619899%5Bcolor%5D=41",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/neutral/product/saucony-mens-everun-freedom-iso-2-running-shoes-viziredblack-332575259.html#332575259%5Bcolor%5D=60",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/product/saucony-mens-everun-freedom-iso-2-running-shoes-white-332575294.html#332575294%5Bcolor%5D=10",
"https://www.sportchek.ca/categories/men/footwear/running-shoes/product/nike-mens-epic-react-flyknit-running-shoes-greywhiteteal-332523370.html#332523370%5Bcolor%5D=04"]
runningroom = ["https://ca.shop.runningroom.com/men/shoes/neutral/saucony-men-s-freedom-iso-running-shoe.html",
"https://ca.shop.runningroom.com/men/new-balance-men-s-fresh-foam-beacon-running-shoe.html",
"https://ca.shop.runningroom.com/men/shoes/neutral/nike-men-s-vomero-13-running-shoe.html",
"https://ca.shop.runningroom.com/men/shoes/neutral/nike-men-s-zoom-pegasus-34-shield-running-shoe.html",
"https://ca.shop.runningroom.com/men/shoes/neutral/brooks-men-s-ghost-11-running-shoe.html"]
mec = ["https://www.mec.ca/en/product/5060-092/Ghost-11-GTX-Road-Running-Shoes","https://www.mec.ca/en/product/5054-659/Ghost-10-Road-Running-Shoes"]

deals = []

for link in sportinglife:
	browser.get(link)

	timeout = 20

	try:
	    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='primary-image']")))
	except TimeoutException:
	    print("*** ERROR: Timed out waiting for page to load ****")
	    #browser.quit()

	print(browser.title)

	element = browser.find_elements_by_xpath("//*[@id='product-content']/div[3]")

	discountprice = [x.text for x in element]

	discountcheck = '%' in str(discountprice)

	if discountcheck == True:
		print('Current Price: ' + str(discountprice) + ' - Discount!' + '\n')
		deals.append(browser.title + ' - Current Price: ' + str(discountprice) + ' - Discount!')
	else:
		print('Current Price: ' + str(discountprice) + ' - Nope!' + '\n')

for link in sportchek:
	browser.get(link)

	timeout = 20

	try:
		WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='product-detail__product-img']")))
	except TimeoutException:
	    print("*** ERROR: Timed out waiting for page to load ***")
	    #browser.quit()

	print(browser.title)

	currentpriceelement = browser.find_elements_by_xpath("//*[@id='product-detail__preview']/div[4]/div[1]/div/span")

	discountappliedelement = browser.find_elements_by_xpath("//*[@id='product-detail__preview']/div[4]/div[3]/div/span/span")

	currentprice = [x.text for x in currentpriceelement]

	discountapplied = [x.text for x in discountappliedelement]

	if not discountappliedelement:
		print('Current Price: ' + str(currentprice) + ' - Nope!' + '\n')
	else:
		print('Current Price: ' + str(currentprice) + ' - Discount! - ' + str(discountapplied) + '\n')
		deals.append(browser.title + ' - Current Price: ' + str(currentprice) + ' - Discount: - ' + str(discountapplied))

for link in runningroom:
	browser.get(link)

	timeout = 20

	try:
		WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='product_addtocart_form']/div[2]/div[2]/p/img[2]")))
	except TimeoutException:
	    print("*** ERROR: Timed out waiting for page to load ***")
	    #browser.quit()

	print(browser.title + ' - Running Room')

	currentpriceelement = browser.find_elements_by_xpath("//*[@id='product_addtocart_form']/div[2]/div[1]/div[1]")

	discountappliedelement = browser.find_elements_by_xpath("//*[@id='product_addtocart_form']/div[2]/div[1]/div[1]/p[2]")

	currentprice = [x.text for x in currentpriceelement]

	discountapplied = [x.text for x in discountappliedelement]

	if not discountappliedelement:
		print('Current Price: ' + str(currentprice) + ' - Nope!' + '\n')
	else:
		print('Current Price: ' + str(currentprice) + str(discountapplied) + ' - Discount!' + '\n')
		deals.append(browser.title + ' - Running Room' + ' - Current Price: ' + str(currentprice) + ' - Discount: ' + str(discountapplied))

for link in mec:
	browser.get(link)

	timeout = 20

	try:
		WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='images']/div[1]/div/div/div/div[1]/div/div/div/img")))
	except TimeoutException:
	    print("*** ERROR: Timed out waiting for page to load ***")
	    #browser.quit()

	print(browser.title + ' - MEC')

	currentpriceelement = browser.find_elements_by_xpath("//*[@id='ProductDetailControls']/div[2]/ul/li")

	discountappliedelement = browser.find_elements_by_xpath("//*[@id='ProductDetailControls']/div[2]/ul/li[1]/span[2]")

	currentprice = [x.text for x in currentpriceelement]

	discountapplied = [x.text for x in discountappliedelement]

	if not discountappliedelement:
		print('Current Price: ' + str(currentprice) + ' - Nope!' + '\n')
	else:
		print('Current Price: ' + str(currentprice) + str(discountapplied) + ' - Discount!' + '\n')
		deals.append(browser.title + ' - MEC' + ' - Current Price: ' + str(currentprice) + ' - Discount: ' + str(discountapplied))

browser.quit()

sendemail(from_addr = login,
    to_addr_list = ['john.tuyen@gmail.com'],
    subject      = 'Daily running shoes deals!', 
    message      = '\n\n'.join(deals),
    login        = login, 
    password     = password)

print("Email sent!")
