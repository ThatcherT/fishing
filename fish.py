from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Firefox()
driver.get("https://irc.chathub.org/dragondyce/")

# wait for the page to load
time.sleep(2)

input_element = driver.find_element_by_class_name("u-input")
input_element.clear()
input_element.send_keys("fisherman-bob")

connect_button = driver.find_element_by_class_name("u-button")
connect_button.click()

# random number between 8 and 15
while True:
    time.sleep(6)
    text_box = driver.find_element_by_class_name("kiwi-ircinput-editor")
    text_box.send_keys("!fish")

    # click enter key
    text_box.send_keys(Keys.RETURN)

    sleep_time = 4 + (8 - 4) * (random.random())
    print("Sleeping for " + str(sleep_time))
    time.sleep(sleep_time * 60)
