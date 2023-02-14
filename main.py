from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
#this allows script to run commands into terminal 
from subprocess import call 

#may need this later
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

URL = input("Please enter the sites URL")

print("checking {URL} for vulnerabilities")
