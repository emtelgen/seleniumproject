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
from spamming import *
from report_info import *

def main_cheat(driver):
    vote = 0
    report_info = driver.find_element_by_class_name('reportDescription').text
    report_details = driver.find_element_by_id('reportContent').get_attribute('innerText')

    guilty_report_details = ['admission', 'admits', 'admits discord', 'admission discord', 'foreign language', 'admitted']
    inno_report_details = ['possible', 'possibly', 'might']
    guilty_messages = ['i am cheating', 'i have hacks', 'discord', 'multiaccounting', 'skype', 'hacks']

    ign = get_ign(driver)
    logs = chatlogs(report_details)
    ind = individual_logs(logs, ign)

    ind_logs = []
    for x in ind:
        ind_logs.append(get_message(x).lower())

    for x in ind_logs:
        for y in guilty_messages:
            if y in x:
                print('Guiltying the Cheating Report: ', get_report_id(driver), ' because the guilty message --', x, ' is found in the guilty chat logs. (', x, ')')
                vote = 1

    if vote == 0:
        for x in guilty_report_details:
            if x in report_info.lower():
                print('Guiltying the Cheating Report: ', get_report_id(driver), 'because the guilty message --', x, 'is found in the report details.')
                vote = 1
    if vote == 0:
        for x in inno_report_details:
            if x in report_info.lower():
                print('Innoing the Cheating Report: ', get_report_id(driver), 'because the inno message --', x, 'is found in the report details')
                vote = 2
    
    return vote
