from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# opens a Google Chrome window
web = webdriver.Chrome()
web.get('https://www.google.com/')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dol = web.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[3]/td[1]/input').get_attribute('data-value')