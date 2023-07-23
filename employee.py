import selenium
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from spamming import *
from voting import *
from report_info import *
from gamethrowing import *
from hsh import *
from leaving import *
from cheating import *
import random

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Path") 
driver = webdriver.Chrome(executable_path='C:\\Users\\mdtelgen\\Desktop\\ScriptFiles\\chromedriver.exe', options = chrome_options)
driver.get("https://www.blankmediagames.com/Trial")
driver.execute_script("document.body.style.zoom='zoom 50%'")

def get_driver():
    return driver

# Determining which report to inno/guilty based on name or ID
guilty_list = ['3411060']
inno_list = ['3414733', '3409550', '3417385', '3417144', '3416991', '3407479']

ended = False

# Click the continue button
continued = False
while not continued:
    try:
        cont = driver.find_element_by_link_text('Continue >>')
        cont.click()
        continued = True
    except (NoSuchElementException, StaleElementReferenceException) as e:
        time.sleep(1)
time.sleep(15)
print('continued')

# Main SCRIPT

while not ended: 

    voted = False
    vote = False
    time.sleep(1)
    #Make sure the report information is viewable
    report_id = get_report_id(driver)
    username = get_name(driver)
    report_date = get_report_date(driver)
    report_reason = get_report_reason(driver)
    report_details = get_report_details(driver)

    format(report_id, username, report_date, report_reason, report_details)

    # Defining the vote variables
    skip = driver.find_element_by_link_text('Skip >>')
    inno = driver.find_element_by_link_text('Innocent')
    guilty = driver.find_element_by_link_text('Guilty')

    # INNOING the report if it equals the report ID

    if report_id in inno_list or username in whitelist:
        print("REPORT IS IN THE INNO LIST OR WHITELIST")
        vote_inno(report_id, driver, inno)
        continue

    elif report_id in guilty_list:
        print("REPORT IS IN THE GUILTY LIST")
        vote_guilty(report_id, driver, guilty)
        continue

    elif report_reason == 'Spamming' and not voted:
        vote = main_spam(driver)

    elif report_reason == 'Gamethrowing' and not voted:
        vote = main_gt(driver, report_details)

    elif report_reason == 'Hate speech/Harassment' and not voted:
        hsh_vote = main_hsh(driver)
        if hsh_vote == 0:
            vote_skip(report_id, driver, skip)
            continue
        elif hsh_vote == 1:
            vote = True
        else:
            vote = False
    
    elif report_reason == 'Cheating' and not voted:
        cheat_vote = main_cheat(driver)
        if cheat_vote == 0:
            vote_skip(report_id, driver, skip)
            continue
        elif cheat_vote == 1:
            vote = True
        else:
            vote = False

    elif report_reason == 'Leaving' and not voted:
        vote = main_leaving(driver)


    else:
        print('Skipping the Report: ', report_id, ' because it is not in a voteable category.')
        vote_skip(report_id, driver, skip)
        continue

    if vote:
        vote_guilty(report_id, driver, guilty)
        time.sleep(random.randint(5, 10))
        voted = True
    elif not vote:
        vote_inno(report_id, driver, inno)
        time.sleep(random.randint(5, 10))
        voted = True
 