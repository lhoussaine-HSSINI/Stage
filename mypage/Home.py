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




@st.cache_resource
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

    driver_1 = webdriver.Chrome(service=ChromeService(executable_path="D:\\chromedriver\\chromedriver.exe"),
                                options=options)
    # driver_1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver_1.get(url)
    time.sleep(3)
    pg=driver_1.page_source
    driver_1.close()
    driver_1.quit()
    return pg

def stocke_data(list_li):
    for i in range(len(list_li)):
        link_job="https://ma.indeed.com"+list_li[i].find("div", {"class":"css-1m4cuuf e37uo190"}).find("a")["href"]
        st.session_state.list_link_job.append(link_job)
        st.markdown(link_job)
        title=list_li[i].find("div", {"class":"css-1m4cuuf e37uo190"}).text
        st.session_state.list_title_jobs.append(title)
        comany_location = list_li[i].find("div", {"class":"companyLocation"}).text
        st.session_state.list_company_location.append(comany_location)
        try:
            company_name = list_li[i].find("span", {"class":"companyName"}).text
        except:
            company_name=None
        st.session_state.list_company_name.append(company_name)


@st.cache_resource
def get_description():
    for url in range(len(st.session_state.list_link_job)):
        resulta = get_pg_source(st.session_state.list_link_job[url])
        soup = BeautifulSoup(resulta, "lxml")
        try:
            discri = soup.find("div", {"id": "jobDescriptionText"}).text
        except:
            discri = ""
        st.session_state.list_discription.append(discri)

def kolchi():
    resulta = get_pg_source("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    soup = BeautifulSoup(resulta, "lxml")
    # st.markdown("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    page_total = soup.find("div", {'class': 'jobsearch-JobCountAndSortPane-jobCount'}).text
    if int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) == 15:
        page_total_of_search = 1
    else:
        page_total_of_search = int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) // 15 + 1
    list_li = soup.findAll("div", {"class": "slider_item css-kyg8or eu4oa1w0"})
    st.markdown(f"number of jobs :::: {page_total_of_search}")
    stocke_data(list_li)
    i_counter = 1
    while True:
        if i_counter < page_total_of_search:
            resulta = get_pg_source("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
            soup = BeautifulSoup(resulta, "lxml")
            list_li = soup.findAll("div", {"class": "slider_item css-kyg8or eu4oa1w0"})
            stocke_data(list_li)
            st.markdown(i_counter)
            i_counter += 1
        else:
            break
    get_description()



def display_data():
    for i in range(len(st.session_state.list_title_jobs)):
        st.markdown(f"""
                <a href="{st.session_state.list_link_job[i]}" class="my-2 card p-4 bg-white border rounded-lg stretched-link">
                  <div class="d-flex align-items-center">
                      <div class="mx-1 ">
                          <img src="https://raw.githubusercontent.com/lhoussaine-HSSINI/Stage/8935dbf0ed54c4ea517deecd02ba8e981de7e0bb/job-seeker.png" alt="aa" width="65" class="rounded-3">  
                      </div>
                      <div class="mx-1">
                          <div class="font-weight-bold leading-tight font-display">{st.session_state.list_title_jobs[i]}</div>
                          <div class="text-muted font-medium text-sm my-1">{st.session_state.list_company_name[i]}</div>
                          <div class="text-muted font-medium text-sm">{st.session_state.list_company_location[i]}</div>
                      </div>
                  </div>
            </a>
            """, unsafe_allow_html=True)

def display_data_as(i:int):
    st.markdown(f"""
            <a href="{st.session_state.list_link_job[i]}" class="my-2 card p-4 bg-white border rounded-lg stretched-link">
              <div class="d-flex align-items-center">
                  <div class="mx-1 ">
                      <img src="https://raw.githubusercontent.com/lhoussaine-HSSINI/Stage/8935dbf0ed54c4ea517deecd02ba8e981de7e0bb/job-seeker.png" alt="aa" width="65" class="rounded-3">  
                  </div>
                  <div class="mx-1">
                      <div class="font-weight-bold leading-tight font-display">{st.session_state.list_title_jobs[i]}</div>
                      <div class="text-muted font-medium text-sm my-1">{st.session_state.list_company_name[i]}</div>
                      <div class="text-muted font-medium text-sm">{st.session_state.list_company_location[i]}</div>
                  </div>
              </div>
        </a>
        """, unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def app():
    lottie_url_download = "https://assets3.lottiefiles.com/packages/lf20_cdhfmdzy.json"
    lottie_download = load_lottieurl(lottie_url_download)
    st.markdown(""" <h1 class='text-center fs-1 headdd'> Bienvenue au FAHO WORK </h1> """, unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(""" <p class='text-center mb-3' style='margin-top: -100px !important;' >  
                 vous pouvez cherchez votre  stage  ou stage pre-embauche dans la platforme</p> """,
                    unsafe_allow_html=True)
    with c2:
        st_lottie(lottie_download, speed=1, reverse=False, loop=True,
                  quality="low", height=None, width=None, key=None)

    if st.session_state.key == 1:
        kolchi()
        # data_get_linkdin()
        st.session_state.key += 1
    st.markdown(len(st.session_state.list_discription))
    st.markdown(len(st.session_state.list_title_jobs))