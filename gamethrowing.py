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
from report_info import *

def main_gt(driver, details):
    detail = ""
    detail_list = []
    determination = 0
    vote = False
    for x in details:
        if x == '\n':
            detail_list.append(detail)
            detail = ""
        else:
            detail += x
    
    for x in detail_list:
        if x == 'None given.':
            vote = False
            print('Innoing the Gamethrowing report: ', get_report_id(driver), ' because no report details were given.')
        elif 'outed' in x.lower():
            vote = True
            print('Guiltying the Gamethrowing report: ', get_report_id(driver), ' because "outed" contained in report details.')
        elif 'claimed evil' in x.lower() or 'claimed maf'in x.lower() or 'claimed witch' in x.lower():
            vote = True
            print('Guiltying the Gamethrowing report: ', get_report_id(driver), ' because "claimed evil" contained in report details.')
        elif 'admission' in x.lower() or 'admits' in x.lower() or 'admitted' in x.lower():
            print('Guiltying the Gamethrowing report: ', get_report_id(driver), ' because "admission" contained in report details.')
            vote = True

    if len(detail_list) > 4:
        print('Guiltying the Gamethrowing report: ', get_report_id(driver), ' because large amount of report details.')
        vote = True
    

    if not vote:
        print('Innoing the report.')
    else:
        print("Guiltying the report.")

    return vote