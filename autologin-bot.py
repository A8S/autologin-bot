#first you need to install selenium and the webdrivers of the respective browser you are using..
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
#network auto-login bot
login_id ='17uec010'#enter you login id here
login_pass ='DxpU3382*'#enter your password
browser = webdriver.Chrome()#choose any other webdriver depending on which  browser you have, here chrome is used.
browser.get(('https://xxx.xxx.xxx.xxx/connect-to-internet-network-access-gain/PortalMain'))#link of the site

username = browser.find_element_by_id('login_id_value')#login_id_value is the id of the text field in which id is to be entered.
username.send_keys(login_id)
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Login_password')))#Login_password is the id of the text field in which password is to be entered
password.send_keys(login_pass)
 
signInButton = browser.find_element_by_id('signIn')
signInButton.click()