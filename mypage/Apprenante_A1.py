import re
import streamlit as st
from mypage import Home
from mypage.Home import display_data_as


def app():
    st.markdown(""" <h1 class='text-center fs-1 headdd'>Search stage</h1> """, unsafe_allow_html=True)
    Categorie_add_1 = st.multiselect('competence',
                                     ['Html', 'Css', 'Java script', 'Php',
                                      'JAVA', 'Python'])
    if Categorie_add_1:
        for i in range(len(st.session_state.list_discription)):
            if re.compile('|'.join(Categorie_add_1), re.IGNORECASE).search(st.session_state.list_discription[i]):
                display_data_as(i)

    else:
        stage_de_embauche = ['pré-embauche', 'pre-embauche', 'rémunéré', 'remunere', 'pre','embauche']
        for i in range(len(st.session_state.list_discription)):
            if re.compile('|'.join(stage_de_embauche), re.IGNORECASE).search(st.session_state.list_discription[i]):
                print("hello")
            else:
                Home.display_data_as(i)

