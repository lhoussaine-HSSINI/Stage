import re
import time
import json
import requests
import streamlit as st
from selenium.webdriver.common.by import By
from streamlit_card import card
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


list_title_jobs=[]
list_company_location=[]
list_company_name=[]
list_discription=[]
list_link_job=[]


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QSob{display: none !important;}
            a {display: none;}
            .leading-tight {
            line-height: 1.25;
        }
        .text-muted {
            --tw-text-opacity: 1;
            color: #6b7280;
            color: rgb(107 114 128/var(--tw-text-opacity));
        }
        .font-medium {
            font-weight: 500;
        }
        .text-sm {
            font-size: .875rem;
            line-height: 1.25rem;
        }
        .font-display {
            font-family: Outfit,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
        }
        a, a:hover{
            text-decoration: none;
        }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
@st.cache_resource
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
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def stocke_data(list_li):
    global list_discription,list_title_jobs,list_company_location,list_company_name,list_link_job
    for i in range(len(list_li)):
        title=list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").text
        list_title_jobs.append(title)
        comany_location=list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='companyLocation']").text
        list_company_location.append(comany_location)
        try:
            company_name =list_li[i].find_element(by=By.CSS_SELECTOR, value="span[class='companyName']").text
        except:
            company_name=None
        list_company_name.append(company_name)
        link_job =list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").find_element(by=By.TAG_NAME, value='a').get_attribute("href")
        list_link_job.append(link_job)
        # st.code(link_job)
        # driver_job=get_driver()
        #
        # # result = requests.get(link_job)
        # # page_source = result.content
        # # soup_product_detaile = BeautifulSoup(page_source, "lxml")
        # # job_description = soup_product_detaile.find('div', {"id": "jobDescriptionText"}).text
        # # list_discription.append(job_description)
        # driver_job.get(link_job)
        # st.code(driver_job.page_source)
        # driver_job.close()

def display_data(list_li):
    for i in range(len(list_li)):
        # st.markdown(list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").text)
        try:
            st.markdown(f"""
                    <a href="{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").find_element(by=By.TAG_NAME, value='a').get_attribute("href")}" class="my-2 card p-4 bg-white border rounded-lg">
                      <div class="d-flex align-items-center">
                          <div class="mx-1 ">
                              <img src="https://raw.githubusercontent.com/lhoussaine-HSSINI/Stage/8935dbf0ed54c4ea517deecd02ba8e981de7e0bb/job-seeker.png" alt="aa" width="65" class="rounded-3">  
                          </div>
                          <div class="mx-1">
                              <div class="font-weight-bold leading-tight font-display">{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").text}</div>
                              <div class="text-muted font-medium text-sm my-1">{list_li[i].find_element(by=By.CSS_SELECTOR, value="span[class='companyName']").text}</div>
                              <div class="text-muted font-medium text-sm">{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='companyLocation']").text}</div>
                          </div>
                      </div>
                </a>
                """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
                                <a href="{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").find_element(by=By.TAG_NAME, value='a').get_attribute("href")}" class="my-2 card p-4 bg-white border rounded-lg">
                                  <div class="d-flex align-items-center">
                                      <div class="mx-1 ">
                                          <img src="https://raw.githubusercontent.com/lhoussaine-HSSINI/Stage/8935dbf0ed54c4ea517deecd02ba8e981de7e0bb/job-seeker.png" alt="aa" width="65" class="rounded-3">
                                      </div>
                                      <div class="mx-1">
                                          <div class="font-weight-bold leading-tight font-display">{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='css-1m4cuuf e37uo190']").text}</div>
                                          <div class="text-muted font-medium text-sm my-1">None</div>
                                          <div class="text-muted font-medium text-sm">{list_li[i].find_element(by=By.CSS_SELECTOR, value="div[class='companyLocation']").text}</div>
                                      </div>
                                  </div>
                            </a>
                            """, unsafe_allow_html=True)

lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_url_download = "https://assets3.lottiefiles.com/packages/lf20_cdhfmdzy.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


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

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(""" <p class='text-center mb-3' style='margin-top: -100px !important;' >  
             vous pouvez cherchez votre  stage  ou stage pre-embauche dans la platforme</p> """,
                    unsafe_allow_html=True)
    with c2:
        st_lottie(lottie_download, speed=1, reverse=False, loop=True,
                  quality="low", height=None, width=None, key=None)



if selected == "Apprenante A2":
    st.markdown(""" <h1 class='text-center fs-1 headdd'>Search stage pre-embauche</h1> """, unsafe_allow_html=True)
    Categorie_add_1 = st.multiselect('competence',
                                     ['Html', 'Css', 'Java script', 'Php',
                                      'JAVA', 'Python',
                                      'Articulations ', ' Rumatismes', 'Minceur & Fermeté', 'Forme & Energie',
                                      'Spécial Femme'])


    # c_1 ,c_2=st.columns(2)
    # with c_1:
    #     hasClicked_1 = card(key=1,
    #         title="Hello World!",
    #         text="Some description",
    #         image="http://placekitten.com/200/300",
    #         url="https://github.com/gamcoh/st-card"
    #     )
    # with c_2:
    # st.markdown("""
    #         <a href="" class="card p-4 bg-white border rounded-lg">
    #           <div class="d-flex align-items-center">
    #               <div class="mx-1 ">
    #                   <img src="https://app.vuejobs.com/storage/1740/d40371ca-c586-4a9a-b5e9-4f6bc21d7e37.com" alt="aa" width="65" class="rounded-3">
    #               </div>
    #               <div class="mx-1">
    #                   <div class="font-weight-bold leading-tight font-display">hello hhhhhhh hhshs</div>
    #                   <div class="text-muted font-medium text-sm my-1">kjcj vkec dcjecc cbbc cuoc uc</div>
    #                   <div class="text-muted font-medium text-sm">Casablanca</div>
    #               </div>
    #           </div>
    #     </a>
    #     """, unsafe_allow_html=True)

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

    display_data(list_li)
    stocke_data(list_li)
    counttt=len(list_li)
    i_counter = 1
    while True:
        if i_counter < page_total_of_search:
            driver.get(f"https://ma.indeed.com/jobs?q=stage+web&fromage=1&start={i_counter}0")
            list_li = driver.find_elements(by=By.CSS_SELECTOR,
                                             value="div[class='slider_container css-g7s71f eu4oa1w0']")
            counttt+=len(list_li)
            # st.markdown(i_counter)
            display_data(list_li)
            stocke_data(list_li)
            i_counter += 1
        else:
            break

    st.markdown(counttt)
    for  ii in range(len(list_link_job)):
        driver.get(list_link_job[ii])
        try:
            time.sleep(2)
            list_linkk = driver.find_element(by=By.ID,value="jobDescriptionText")
            list_discription.append(list_linkk.text)
        except:
            list_discription.append(None)



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
