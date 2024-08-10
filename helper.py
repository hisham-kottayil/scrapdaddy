import streamlit as st
from st_pages import Page, show_pages, add_page_title, hide_pages


def hide_pages_dynamically(authentication_status):
    if not authentication_status:
        hide_pages(
            ["Materials", "Vehicle", "Address", "Checkout", "My Orders"]
            )
    else:
        pass