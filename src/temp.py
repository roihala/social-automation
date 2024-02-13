#!/usr/bin/python3
import os, sys
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import time

from tiktok_uploader.browsers import get_browser

MINUTES, SECONDS =60, 60
DELAY_HOURS = 4
DELAY_START_SECONDS= 120

IsLinux = False
username = "roihalamish@gmail.com"
password = "Hala!564"
login_url = "https://my.yad2.co.il/login.php"
ad_url_pattern = "https://my.yad2.co.il/newOrder/index.php?action=personalAreaViewDetails&CatID=3&SubCatID=0&OrderID={ad_id}"

# ads dictionary should be composed as the following format ad id: ad nickname
ads = {"41445438": "Mad molijut",
       "43011565": "BBQ", "43228689": "Red couch", "43228711": "Black couch", "43228664": "Gray couch",
       "43282531": "Quest 2"
       }

if __name__ == "__main__":

    os.chdir(os.path.dirname(sys.argv[0]))
    driver = None, None

    while True:
        try:
            starttime = time()

            driver = get_browser()
            driver.get(login_url)  # if using on premise LAN and receive error 502 - not using correct proxy.
            username_input = driver.find_element(By.ID, "email")
            password_input = driver.find_element(By.ID, "password")

            username_input.send_keys(username)
            sleep(4)
            password_input.send_keys(password + Keys.ENTER)
            # End of login
            sleep(5)
            for ad_id, ad_name in ads.items():
                try:
                    driver.get(ad_url_pattern.format(ad_id=ad_id))
                    sleep(1)
                    click_span = driver.find_element_by_id("bounceRatingOrderBtn")
                    click_span.click()
                    now = datetime.now()
                    print(f"{now.strftime('%H:%M:%S')} ad {ad_name} id: {ad_id} done")
                except:
                    print(f"{now.strftime('%H:%M:%S')} ad {ad_name} id: {ad_id} failed")
                sleep(1)
            driver.quit()
        except Exception as e:
            print(f"Error {e}, skipping this time and going to sleep!")
        print("Sleeping....")
        while True:  # we check the time because if the computer sleeps the sleep time don't count.
            sleep(30)
            if time() - starttime > DELAY_HOURS * MINUTES * SECONDS  + DELAY_START_SECONDS:
                break
        print("Good morning")