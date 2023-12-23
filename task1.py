from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import json

gmail_username = input("your email id:")
gmail_password = input('your password: ')
driverinput=input(" Chrome(1),Edge(2),Firefox(3)(select the brower using number):  ")
if driverinput == '1':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
elif driverinput == '2':
    driver= webdriver.Edge()
elif driverinput =='3':
    driver= webdriver.Firefox()
else:
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    
    driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail&ec=GAlAFw&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-653330188%3A1703316598942734&theme=glif")

    
    username_field = driver.find_element("id", "identifierId")
    username_field.send_keys(gmail_username)
    username_field.send_keys(Keys.RETURN)

    
    time.sleep(2)

    driver.find_element("id","identifierNext")
    time.sleep(20)

    password_field = driver.find_element("class", "whsOnd zHQkBf")
    password_field.send_keys(gmail_password)
    password_field.send_keys(Keys.RETURN)

    
    
    inbox_link = driver.find_element("link text", "Inbox")
    inbox_link.click()

    
    time.sleep(2)

   
    first_email = driver.find_element("css selector", "div.xT")
    first_email.click()

    time.sleep(3)

   
    top_ten_emails = []
    for i in range(10):
        email_subject = driver.find_element("css selector", "h2.hP").text
        email_body = driver.find_element("css selector", "div.a3s.aiL").text

        email_data = {"subject": email_subject, "body": email_body}
        top_ten_emails.append(email_data)

    
        next_email_button = driver.find_element("css selector", "div.asa")
        next_email_button.click()

        time.sleep(3)

    with open("top_ten_emails.json", "w") as json_file:
        json.dump(top_ten_emails, json_file, indent=2)

finally:
    
    driver.quit()
