import streamlit as st
from .upload_ui import ContentUpload
from .chatbot import AlippoAssistant

class Routes:
    def home(self):
        with open('README.md') as f:
            home_text = f.read()
        st.markdown(home_text)
    
    def upload_content(self):
        uploaded_content = ContentUpload().run_content_upload()
    
    def alippo_assistant(self):
        # some how we need to connect the user of when to use text and when
        # to use images and some signal after which the user uploads the image
        uploader = ContentUpload()
        inline_chat_upload = uploader.upload_content()
        if inline_chat_upload:
            uploader._plot_images_to_be_post(inline_chat_upload)
        assistant = AlippoAssistant().chat_component()