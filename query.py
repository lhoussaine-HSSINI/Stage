import re
import time
import threading
import streamlit as st
import requests
from streamlit_lottie import st_lottie

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

def get_pg_source(url:str):
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
    #
    # driver_1 = webdriver.Chrome(service=ChromeService(executable_path="D:\\chromedriver\\chromedriver.exe"),
    #                             options=options)
    driver_1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver_1.get(url)
    pg=driver_1.page_source
    driver_1.close()
    driver_1.quit()
    return pg


def gettt():
    resulta=get_pg_source("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    soup = BeautifulSoup(resulta, "lxml")
    st.markdown("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    page_total = soup.find("div", {'class':'jobsearch-JobCountAndSortPane-jobCount'}).text
    if int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) == 15:
        page_total_of_search = 1
    else:
        page_total_of_search = int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) // 15 + 1
    list_li = soup.findAll("div", {"class":"slider_item css-kyg8or eu4oa1w0"})
    st.markdown(f"number of jobs :::: {page_total_of_search}")
    st.markdown(len(list_li))
gettt()