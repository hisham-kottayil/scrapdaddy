import streamlit as st
from st_pages import Page, add_page_title, hide_pages


def hide_pages_dynamically(authentication_status):
    if not authentication_status or authentication_status == '':
        print("Here")
        hide_pages(
            ["Materials", "Vehicle", "Address", "Checkout", "Orders"]
            )
    else:
        pass
    
def hide_pages_extras():
    hide_pages(
        ["styles", "Test"]
        )