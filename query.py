import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import  streamlit as st
import requests
from webdriver_manager.chrome import ChromeDriverManager


def gettt():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument("--test-type")
    options.add_argument('--log-level=3')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--mute-audio")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-blink-features=AutomationControlled')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    # driver_linkdin = webdriver.Chrome(service=ChromeService(executable_path="D:\\chromedriver\\chromedriver.exe"), options=options)
    driver_linkdin = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver_linkdin.get("https://www.linkedin.com/jobs/")
    time.sleep(3)
    email = driver_linkdin.find_element(by=By.ID, value="session_key")
    email.clear()
    email.send_keys("bontop.2018@gmail.com")
    password = driver_linkdin.find_element(by=By.ID, value="session_password")
    password.clear()
    password.send_keys("T8<)_mc~/xXEZ:7")
    time.sleep(3)
    submit_login = driver_linkdin.find_element(by=By.CLASS_NAME, value="sign-in-form__submit-button")
    submit_login.click()
    time.sleep(10)
    # driver_linkdin.close()
    st.code(driver_linkdin.page_source)


    # time.sleep(10)
    # driver_linkdin.get("https://www.linkedin.com/jobs/search/?currentJobId=3492533221&f_TPR=r86400&geoId=102787409&keywords=Stage%20PFE&location=Morocco&refresh=true")
    # time.sleep(5)


gettt()