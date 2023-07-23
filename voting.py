import selenium
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains  import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def vote_inno(report_id, driver, inno):
    innoing = False
    while not innoing:
        try:
            inno.click()
            time.sleep(1)
            driver.switch_to.alert.accept()
            innoing = True
            time.sleep(1)
            driver.find_element_by_id('modalClose').send_keys(u'\ue007')
            time.sleep(1)
        except ElementClickInterceptedException:
            time.sleep(1)
    print("Script has INNOED Report: ", report_id)
    print("\n")
    time.sleep(1)

def vote_guilty(report_id, driver, guilty):
    guiltying = False
    while not guiltying:
        try:
            guilty.click()
            driver.switch_to.alert.accept()
            guiltying = True
            time.sleep(1)
            driver.find_element_by_id('modalClose').send_keys(u'\ue007')
            time.sleep(1)
        except ElementClickInterceptedException:
            time.sleep(1)
    print("Script has GUILTIED Report: ", report_id)
    print("\n")
    time.sleep(1)

def vote_skip(report_id, driver, skip):
    skipped = False
    while not skipped:
        try:
            skip = driver.find_element_by_link_text('Skip >>')
            skip.click()
            skipped = True
        except ElementClickInterceptedException:
            time.sleep(1)
    print("Script has SKIPPED Report: ", report_id)
    print("\n")
    time.sleep(1)