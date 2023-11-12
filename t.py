import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login")
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("xuser123") #replace with your twitter account 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password") 
password.send_keys("Twitter123")#replace with your twitter password 
password.send_keys(Keys.ENTER)
time.sleep(4)
driver.get('https://twitter.com/samuraipreneur') #replace with username which you want to report that account after .com/
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div').click()#id click
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[5]').click()#report
time.sleep(3)
driver.execute_script('document.querySelector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-1ifxtd0 > div > div > label:nth-child(1) > div.css-1dbjc4n.r-6uxfom.r-lrvibr > input[type=radio]").click()')#start report
time.sleep(3)
driver.execute_script('document.querySelector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-9hvr93.r-1isdzm1 > div > div > div > div > div").click()') #click on next button
#after these they will ask again with option select one next click and submit and done (we can write code for that,but everytime the code changes when twitter got update)
time.sleep(20)
