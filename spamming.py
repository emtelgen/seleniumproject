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

def get_ign(driver):
    full_name_id = driver.find_element_by_class_name("reportedPlayer").text
    full_ign = ""
    ign_up = False
    for x in range(1, len(full_name_id)):
        if(full_name_id[x-1] == '('):
            ign_up = True
        elif(full_name_id[x] == ')'):
            ign_up = False

        if ign_up:
            full_ign += full_name_id[x]
    return full_ign

def get_message(full_message):
    message = ""
    filler = ['-', '=', '~', '!', '.', '?', '*', '@', '#']
    status = False
    for x in range(0, len(full_message)):
        if full_message[x-2] == ':':
            status = True
        if 'Day' in full_message and len(full_message) < 7:
            return 'Day'
        elif status and full_message[x] not in filler:
            message += full_message[x]

    return message

def chatlogs(report_info):
    elements = []
    add_element = ""
    for x in range(0, len(report_info)):
        if report_info[x] != '\n':
            add_element += report_info[x]
        else:
            elements.append(add_element)
            add_element = ""
    return elements

def individual_logs(elements, ign):
    user_elements = []
    defense = False
    for x in range(0, len(elements)):
        user = ""
        status = True

        #Getting the IGN of the person speaking
        for y in range(0, len(elements[x])):
            if elements[x][y] == ":":
                status = False
                y = len(elements[x]) - 1
            if status:
                user += elements[x][y]

        #Don't count messages on defense stage
        if user == 'Defense':
            defense = True
        #Begin to count again once defense has ended
        elif 'Judgement' in user:
            defense = False
        #Determine if the reported user typed the message and add it to list if so
        if not defense:
            if user == ign:
                user_elements.append(elements[x])
            elif 'Day' in user and len(user) == 5:
                user_elements.append('Day')

    return user_elements

def spam(name, ign, driver):
    report_info = driver.find_element_by_id('reportContent').get_attribute('innerText')
    elements = chatlogs(report_info)
    user_elements = individual_logs(elements, ign)
    for x, val in enumerate(user_elements):
        spam = 0
        message = get_message(val)
        if message != 'Day':
            for y, val2 in enumerate(user_elements):
                if x != y:
                    second_message = get_message(val2)
                    if message in second_message:
                        spam += 1
                        if spam >= 4:
                            print('Guiltying the Spamming Report: ', get_report_id(driver), 'because the spam counter hit 4.')
                            return True
                    elif second_message == 'Day':
                        spam = 0
    print('Innoing the Spamming Report: ', get_report_id(driver), 'because the spam counter did not hit 4.')
    return False
    
def main_spam(driver):
    username = get_name(driver)
    ign = get_ign(driver)
    vote = spam(username, ign, driver)
    return vote

