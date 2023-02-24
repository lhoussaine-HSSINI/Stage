import streamlit as st
from mypage import Apprenante_A2, Apprenante_A1, Home
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Faho App", page_icon="🤖")
# Create an empty list to store values in session
if 'list_discription' not in st.session_state:
    st.session_state['list_discription'] = []
    st.session_state['list_title_jobs'] = []
    st.session_state['list_company_location'] = []
    st.session_state['list_company_name'] = []
    st.session_state['list_link_job'] = []


def css_my_ap_all():
    # start my css in header
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
            .css-1gk2i2l ,.e17lx80j0 {visibility: hidden;}
            .css - 4 z1n4l,.ehezqtx5 {visibility: hidden;} 
            .viewerBadge_container__1QSob {visibility: hidden;}
            body {background-color: #fff !important;}
                </style>
                """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
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
    # end my css in header

with st.sidebar:
    selected = option_menu(None, ["Home","Apprenante A2", "Apprenante A1"],
                            icons=['house', 'person-workspace', 'person-workspace'], default_index=0,
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "nav-link": {"font-size": "14px!important", "text-align": "center", "margin": "0px",
                                             "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "green", "font-size": "16px!important"},
                                "viewerBadge_container__1QSob" :{"visibility": "hidden !important"}
                            }
                            )



def js_my_app():
    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)

def main():
    if selected =="Home":
        Home.app()

    if selected == "Apprenante A2":
        Apprenante_A2.app()
    if selected == "Apprenante A1":
        Apprenante_A1.app()


if __name__ == "__main__":
    if 'key' not in st.session_state:
        st.session_state['key'] = 1
    css_my_ap_all()
    main()
    js_my_app()

