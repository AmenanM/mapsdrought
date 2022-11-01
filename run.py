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
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()