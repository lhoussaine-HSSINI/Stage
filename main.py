import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

import streamlit as st
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import requests
from streamlit_card import card
from streamlit_card import _streamlit_card
from streamlit_option_menu import option_menu
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

options = Options()
options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument('--headless')
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("disable-blink-features")
options.add_argument("disable-blink-features=AutomationControlled")
options.add_argument("--disable-3d-apis")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
            'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
            'crossorigin="anonymous">',
            unsafe_allow_html=True)
st.markdown('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"'
            ' integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"'
            ' crossorigin="anonymous"></script>', unsafe_allow_html=True)

@st.cache_resource
def get_driver():
    S = Service("chromedriver/chromedriver.exe")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
    return webdriver.Chrome(options=options)
    # return driver     return webdriver.Chrome(service=S, options=options)
@st.cache_resource
def get_ofre_stage_indeed():
    driver_inded = get_driver()
    key_search="stage web"
    driver_inded.get('https://ma.indeed.com/jobs?q=stage+web&fromage=1')
    time.sleep(10)
    list_page=[]
    # driver_inded.find_element(by=By.CSS_SELECTOR, value="span[class='mark']").click()
    time.sleep(10)
    list_page_sel=driver_inded.find_elements(by=By.CSS_SELECTOR, value="div[class='css-tvvxwd ecydgvn1']")
    page_total = driver_inded.find_element(by=By.CLASS_NAME, value="jobsearch-JobCountAndSortPane-jobCount").text
    page_total_of_search = int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) // 15 + 1
    st.markdown(page_total)
    st.markdown(page_total_of_search)


    # key_word=driver_inded.find_element(by=By.ID,value='text-input-what')
    # key_word.clear()
    # key_word.send_keys("stage web")
    # list_page=driver_inded.find_elements(by=By.CLASS_NAME, value="css-tvvxwd ecydgvn1")
    # key_button.click()
    # driver_inded.find_element(by=By.ID, value="filter-dateposted").click()
    # driver_inded.find_element(by=By.CLASS_NAME,value="")


styl = f"""
    <style>
        .headdd{{
                    margin-top: -100px !important;
        }}
    </style>
    """
st.markdown(styl, unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu(None, ["Home","Apprenante A2", "Apprenante A1"],
                            icons=['house', 'person-workspace', 'person-workspace'], default_index=0,
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "nav-link": {"font-size": "14px!important", "text-align": "center", "margin": "0px",
                                             "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "green", "font-size": "16px!important"},
                            }
                            )

if selected =="Home":
    st.markdown(""" <h1 class='text-center fs-1 headdd'> Bienvenue au FAHO WORK </h1> """,  unsafe_allow_html=True)
    st.markdown(""" <p class='text-center mb-3' style='margin-top: -100px !important;' >  
     vous pouvez cherchez votre  stage  ou stage pre-embauche dans la platforme</p> """,  unsafe_allow_html=True)
if selected == "Apprenante A2":
    st.markdown(""" <h1 class='text-center fs-1 headdd'>Search stage pre-embauche</h1> """, unsafe_allow_html=True)
    get_ofre_stage_indeed()
    Categorie_add_1 = st.multiselect('competence',
                                     ['Html', 'Css', 'Java script', 'Php',
                                      'JAVA', 'Python',
                                      'Articulations ', ' Rumatismes', 'Minceur & Fermeté', 'Forme & Energie',
                                      'Spécial Femme'])


    c_1 ,c_2=st.columns(2)
    with c_1:
        hasClicked_1 = card(key=1,
            title="Hello World!",
            text="Some description",
            image="http://placekitten.com/200/300",
            url="https://github.com/gamcoh/st-card"
        )
    with c_2:
        hasClicked_2 = card(key=2,
            title="Hello World!",
            text="Some description",
            image="http://placekitten.com/200/300",
            url="https://github.com/gamcoh/st-card"
        )


if selected == "Apprenante A1":
    st.markdown(""" <h1 class='text-center fs-1 headdd'>Search stage</h1> """, unsafe_allow_html=True)
    get_ofre_stage_indeed()
    Categorie_add_1 = st.multiselect('competence',
                                     ['Html', 'Css', 'Java script', 'Php',
                                      'JAVA', 'Python',
                                      'Articulations ', ' Rumatismes', 'Minceur & Fermeté', 'Forme & Energie',
                                      'Spécial Femme'])


# options = Options()
# options.add_experimental_option('prefs', {
#     'credentials_enable_service': False,
#     'profile': {
#         'password_manager_enabled': False
#     }
# })
# options.add_experimental_option("useAutomationExtension", False)
# # options.add_argument('--headless')
# # options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-features=NetworkService")
# options.add_argument("--window-size=1920x1080")
# options.add_argument("--disable-features=VizDisplayCompositor")
#
# driver = get_driver()
# driver.get('https://ma.indeed.com/')
# email=driver.find_element(by=By.ID,value='email')
# email.clear()
# email.send_keys("h.lhoussaine@student.youcode.ma")
# password=driver.find_element(by=By.ID, value="password")
# password.clear()
# password.send_keys("GNc7TPtDpNWZ2tk")
# time.sleep(3)
# btn_login=driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div[2]/div[2]/form/div[6]/button")
# btn_login.click()
# time.sleep(3)
# btn=driver.find_element(by=By.XPATH, value="//*[@id='sidebar']/div/div[1]/div[4]/a/div[2]")
# btn.click()
# # apprenante_total = driver.find_elements(By.TAG_NAME, value='a')
# time.sleep(4)
#
#
#
#
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# aa=len(driver.execute_script("return document.getElementsByClassName('account-profile-photo bg-gray-600')"))
# liens = driver.find_elements(By.CSS_SELECTOR, "div[class='card mt-2 mb-2 text-center bg-light shadow-sm']")
# list_image=[]
# list_nom=[]
# for i in range(len(liens)):
#     print(liens[i].find_element(By.CSS_SELECTOR, "div[class='account-profile-photo bg-gray-600']"))
#     list_image.append(liens[i].find_element(By.CSS_SELECTOR, "div[class='account-profile-photo bg-gray-600']"))
#     list_nom.append(liens[i].find_element(By.CSS_SELECTOR, "h5[class='card-title text-truncate']").get_attribute("title"))
#
# st.markdown(liens)
#
# driver.close()




# st.markdown(page_source)
# soup=BeautifulSoup(page_source, "lxml")
# st.markdown(soup)
# lien_image=soup.find("a", {"class":"gb_e gb_0a gb_r"})
# .find("img")["src"]

# apprenant_all=soup.find_all("div", {"class":"card mt-2 mb-2 text-center bg-light shadow-sm"})
#
# for i in range(len(apprenant_all)):
#     list_image.append(apprenant_all[i].find("img")["src"])
#     list_nom.append(apprenant_all[i].findNext("h5", {"class":"card-title text-truncate"}).text)


#
# st.markdown(list_image)
# st.markdown(list_nom)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)