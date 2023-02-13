import re
import time

import streamlit as st
from selenium.webdriver.common.by import By
from streamlit_card import card
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QSob{display: none !important;}
            a {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.experimental_singleton
def get_driver():
    driver_1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver_1, 20)
    action = ActionChains(driver_1)
    return driver_1

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



st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
            'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
            'crossorigin="anonymous">',
            unsafe_allow_html=True)
st.markdown('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"'
            ' integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"'
            ' crossorigin="anonymous"></script>', unsafe_allow_html=True)






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

    driver = get_driver()
    # driver.get("https://ma.indeed.com")
    # time.sleep(5)
    driver.get("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    # driver.find_element(by=By.CSS_SELECTOR, value="span[class='mark']").click()
    page_total = driver.find_element(by=By.CLASS_NAME, value="jobsearch-JobCountAndSortPane-jobCount").text
    page_total_of_search = int([int(s) for s in re.findall(r'-?\d+\.?\d*', page_total)][-1]) // 15 + 1
    list_li=driver.find_elements(by=By.CSS_SELECTOR, value="div[class='slider_container css-g7s71f eu4oa1w0']")
    st.markdown(page_total)
    st.markdown(page_total_of_search)

    st.code(list_li)

if selected == "Apprenante A1":
    st.markdown(""" <h1 class='text-center fs-1 headdd'>Search stage</h1> """, unsafe_allow_html=True)
    Categorie_add_1 = st.multiselect('competence',
                                     ['Html', 'Css', 'Java script', 'Php',
                                      'JAVA', 'Python',
                                      'Articulations ', ' Rumatismes', 'Minceur & Fermeté', 'Forme & Energie',
                                      'Spécial Femme'])







st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
