from typing import List
from bokeh import themes
from bokeh.themes import theme
import streamlit as st
from streamlit import config
from streamlit import config_option
from streamlit.elements.layouts import SpecType
from streamlit.proto.NewReport_pb2 import Config
from streamlit.state.session_state import LazySessionState, SessionState, SessionStateStatProvider, WidgetCallback, WidgetKwargs, get_session_state
from streamlit.type_util import Key
from streamlit.uploaded_file_manager import UploadedFile, UploadedFileManager
from transcribe import *
import time
import numpy as np
import pandas as pd
from views import *
from PIL import Image
import plotly.graph_objects as go
import json

st.title("AI Powered Transcription Service")
st.write(
    """ Our A.I. powered Voice & Video transcription service already integrates with other advanced Human Automation A.I Speech-to-Text Services (API),
    We bringing this service to support & grown South Africans who are already connected to the Internet, Already South African interent usage is sitting with over million users online(Internet) searching for Music,Movies,Games,Work. However,
    in this case, Emazweni Web Services (Pty) Ltd will provide its live, interactive transcripts
    and video captions by way of a Chrome web browser extension and other Web browser Extension Services."""
)
st.header("Trascribe Your Audio Files")

fileObject = st.file_uploader(label="Please upload your file")
                              
if fileObject:
    token, t_id = upload_file(fileObject)
    bytesdata = fileObject.getvalue()
    st.write(bytesdata)
    result = {}
    #polling
    sleep_duration = 1
    percent_complete = 0
    progress_bar = st.progress(percent_complete)
    st.info("Currently in queue")
    while result.get("status") != 'processing':
        percent_complete += sleep_duration
        time.sleep(sleep_duration)
        progress_bar.progress(percent_complete / 10)
        result = get_text(token, t_id)
    sleep_duration = 0.01
    for percent in range(percent_complete, 101):
        time.sleep(sleep_duration)
        progress_bar.progress(percent)
    with st.spinner('processing'):
        while result.get("status") != 'completed':
            result = get_text(token, t_id)
    st.balloons()
    st.header("Transcribed Text")
    st.write(result['text'])
    result = get_text(result.split('\n',1)[0])
#Sidebar Nav Menue
with st.sidebar:
    #image = Image.open("./img/iconlogo.png")
    #st.image(image, width=175, caption=""" 'A.I Powered Transcription ' """)
    st.title("MY TRANSCRIPTION")
    st.header("DOCUMENTS")
    contact = st.button(label="CONTACT")

#Form Submission Function
st.sidebar.info('CLIENT ZONE')
with st.sidebar:

    st.sidebar.info("CLIENT REGISTER")
    st.sidebar.button('Sign_up')
    st.title('👑Premium Membership:')
    st.success("Video-To-Text Transcription")
    st.warning("Speech-To-Text Transcription")
    st.info("Real Time Transcription")
#User File Resource Details
st.subheader("User File Details",
             anchor="https://api.assemblyAI.com/user-details-data")
st.write(
    pd.DataFrame({
        'Format Type': ["mp3", "wav", "mpg", "mp3"],
        'Files Transcribed': [10, 20, 30, 40]
    }))

#User Data Analytics function
st.title('Analytics')

