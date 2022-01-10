import os
from bokeh.embed.standalone import file_html
import requests
import streamlit as st


def about():
    page = open('./views/about.html', 'r', bool=False, encoding='utf-8')
    about_res = page.read()
    return (about_res)


def services():
    services_res = file_html(template='./views/services.html', bool=False)
    return (services_res)


def contacts():
    contact_res = file_html(template='./views/contact.html', bool=False)
    return (contact_res)


def show():

    def about():
        st.session_state['about_res'] = 'about'

    def services():
        st.session_state['service_res'] = 'services'

    def contacts():
        st.session_state['contact_res'] = 'contacts'


show()