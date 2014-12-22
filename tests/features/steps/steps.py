from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import contextlib

@when('we visit https://crash-stats.mozilla.com/')  
def step(context): 
   context.browser.get("https://crash-stats.mozilla.com/")  
 
@then('it should have a title "Crash Data for Firefox"')  
def step(context):  
    assert context.browser.title == "Crash Data for Firefox"
    
@then('there should be a search bar')
def step(context):
    assert "Firefox  Crash Data" in context.browser.find_elements_by_id('homepage-heading')