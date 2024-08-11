import streamlit as st
from st_pages import Page, add_page_title, hide_pages


def hide_pages_dynamically(authentication_status):
    if not authentication_status or authentication_status == '':
        st.write("Here")
        hide_pages(
            ["Materials", "Vehicle", "Address", "Checkout", "Orders"]
            )
    else:
        st.write('Here2')
        pass
    
def hide_pages_extras():
    hide_pages(
        ["styles", "Test"]
        )