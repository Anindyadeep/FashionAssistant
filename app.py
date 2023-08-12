import streamlit as st
from src.config import METADATA_STORE, JSON_PATH
from components.routes import Routes

def app():
    routes = Routes()
    pages = {
        'Home': routes.home,
        'Upload Content': routes.upload_content,
        'Ask Assistant': routes.alippo_assistant
    }
    st.sidebar.title('Navigate')
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page with page function
    pages[page]()



if __name__ == '__main__':
    app()