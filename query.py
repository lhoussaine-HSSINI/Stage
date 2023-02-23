import time
import  streamlit as st
import requests
from bs4 import BeautifulSoup



def gettt():
    resulta=requests.get("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    soup = BeautifulSoup(resulta.content, "lxml")
    st.code(soup)
gettt()