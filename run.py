#app.py
import historical
import proj
import fig
import streamlit as st
PAGES = {
    "hist": historical,
    "proj": proj,
    "fig":fig
}
st.sidebar.title('Navigation')
st.set_page_config(page_icon="./Q quant logo.png", page_title="Quant AI Lab", layout="wide",
                   initial_sidebar_state="expanded")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
