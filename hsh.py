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

def main_hsh(driver):
    vote = 0

    guilty_report_details = ['in real life', 'irl',  'filter evasion', 'link', 'racist', 
    'ddos', 'ip address']
    inno_report_details = ['inciting false reports', 'reghunting']

    report_details = driver.find_element_by_id('reportContent').get_attribute('innerText')
    report_info = driver.find_element_by_class_name('reportDescription').text

    ign = get_ign(driver)
    logs = chatlogs(report_details)
    ind = individual_logs(logs, ign)

    ind_logs = []
    for x in ind:
        ind_logs.append(get_message(x).lower())


    for x in guilty_report_details:
        if x in report_info.lower():
            print('Guiltying the HS/H Report: ', get_report_id(driver), ' because the report details contain a guilty detail (', x, ')')
            vote = 1

    if vote == 0:
        for x in inno_report_details:
            if x in report_info.lower():
                print('Innoing the HS/H Report: ', get_report_id(driver), ' because the report details contain an inno detail (', x, ')')
                vote = 2

    return vote

    