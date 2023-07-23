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

def get_report_id(driver):
    empty = False
    found = False
    while not empty:
        while not found:
            try:
                report_id = driver.find_element_by_class_name("reportId").text
                if report_id != '--':
                    empty = True
                    found = True   
            except NoSuchElementException:
                time.sleep(1)
    return report_id

def get_name(driver):
    full_name_id = driver.find_element_by_class_name("reportedPlayer").text
    name_id = ""
    name_up = False
    for x in range(1, len(full_name_id)):
        if full_name_id[x-1] == " ":
            if name_up == True:
                break
            else:
                name_up = True
        if name_up and full_name_id[x] != ' ':
            name_id += full_name_id[x]
    return name_id 

def get_report_date(driver):
    report_date = driver.find_element_by_class_name("reportDate").text
    return report_date

def get_report_reason(driver):
    report_reason = driver.find_element_by_class_name('reportReason').text
    return report_reason

def get_report_details(driver):
    report_details = driver.find_element_by_class_name('reportDescription').text
    return report_details

def format(report_id, username, report_date, report_reason, report_details):
    print("Report ID: ", report_id)
    print("Username: ", username)
    print("Report Date: ", report_date)
    print("Report Reason: ", report_reason)
    print("Report Details: ", report_details)
    print("\n")