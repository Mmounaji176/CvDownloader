from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time


path = "C:\Program Files\chromedriver.exe"
driver= webdriver.Chrome(path)

driver.get("https://www.linkedin.com/")

#login part
linkedin_mail ="mounajimouad@gmail.com"
linkedin_password ="chaosisdaname@99"


main_field =driver.find_element_by_name("session_key")
passwrd_field =driver.find_element_by_name("session_password")


main_field.send_keys(linkedin_mail)
passwrd_field.send_keys(linkedin_password)
passwrd_field.send_keys(Keys.RETURN)

#searching for people

search_field = driver.find_element_by_id("global-nav-search") #click on the search field first
search_field.click()

search = driver.find_element_by_tag_name("input")
search.send_keys("baddi youssef")
search.send_keys(Keys.RETURN)
time.sleep(2)

name = driver.find_elements_by_class_name("app-aware-link")
names =[lnk for lnk in name]
names[0].click()
time.sleep(2)
#download the cv
plus_button = driver.find_elements_by_tag_name("span")
for pls in plus_button:
    if pls.text =="Plus":
        pls.click()

time.sleep(1)
upload_field = driver.find_element_by_css_selector(".artdeco-dropdown__content-inner ul li:nth-child(2)")
upload_field.click()


















   
