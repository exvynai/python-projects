from selenium import webdriver
import time

username = input("Enter the username: ")
msg = input("Enter the message: ")
times = input("Enter the number of times to spam(type 'infinite' if you want to spam forever): ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://web.whatsapp.com/')
time.sleep(30)

user = driver.find_element_by_xpath(f'//span[@title="{username}"]')
user.click()

if times == 'infinite':
    while True:
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        msg_box.send_keys(msg)

        send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        send.click()
else:
    for i in range(int(times)):
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        msg_box.send_keys(msg)

        send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        send.click()





