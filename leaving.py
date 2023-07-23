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



def main_leaving(driver):
    report_info = driver.find_element_by_class_name('reportDescription').text
    vote = False
    if 'admission' in report_info or 'admits' in report_info or 'admitted' in report_info or 'last will' in report_info:
        print('Guiltying the Leaving Report: ', get_report_id(driver), 'because the admission was found in the report details')
        vote = True

    return vote
