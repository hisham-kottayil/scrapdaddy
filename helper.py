import streamlit as st
from st_pages import Page, add_page_title, hide_pages


def hide_pages_dynamically(authentication_status):
    if not authentication_status:
        st.write("Here1")
        st.sidebar.page_link('Enviro.py', label='Enviro', background_color="#007BFF")
        st.sidebar.page_link('pages/2_Login.py', label='Login')
        st.sidebar.page_link('pages/3_Signup.py', label='Signup')
        st.sidebar.page_link('pages/9_About.py', label='About')
        # hide_pages(
        #     ["3_Signup", "Signup", "signup", "4_Materials", "Vehicle", "Address", "Checkout", "Orders", "styles"]
        #     )
    else:
        st.write('Here2')
        st.sidebar.page_link('Enviro.py', label='Enviro')
        st.sidebar.page_link('pages/2_Login.py', label='Login')
        st.sidebar.page_link('pages/3_Signup.py', label='Signup')
        st.sidebar.page_link('pages/4_Materials.py', label='Materials')
        st.sidebar.page_link('pages/5_Vehicles.py', label='Vehicles')
        st.sidebar.page_link('pages/6_Address.py', label='Address')
        st.sidebar.page_link('pages/7_Checkout.py', label='Checkout')
        st.sidebar.page_link('pages/8_Orders.py', label='Orders')
        st.sidebar.page_link('pages/9_About.py', label='About')
    
def hide_pages_extras():
    hide_pages(
        ["styles", "Test"]
        )
    
def load_sidebar_styles():
    return """
        <style>
        div[data-testid="stSidebarNav"] li div a {
            margin-left: 1rem;
            padding: 0.5rem;
            width: 200px;
            font-color: #ffffff;
            border-radius: 0.25rem;
            background-color: rgba(218, 247, 241, 1);
            /* border: 1px solid lightgrey; */
        }

        div[data-testid="stPageLink-NavLink"] li div a {
            background-color: rgba(151, 166, 195, 0.15);
        }
        [data-testid="stSidebarContent"] {
            background-color: #f7f8fa;
            padding: 20px;
            border-radius: 10px;
            font-size: 16px;
        }
        [data-testid="stSidebarHeader"] {
        /* Add your desired styles here */
        padding: 20px;
        height: 100px;
        }      
        </style>
        """
        
def load_home_button_styles():
    return """
        <style>
        .category-button {
            display: flex;
            align-items: center;
            justify-content: center; /* Center the text and image */
            background-color: rgb(35, 172, 160);
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
            padding: 10px 20px;
            margin: 10px 0;
            font-size: 15px; /* Adjust font size */
            font-family: Arial, sans-serif;
            color: white !important;
            margin-left: 20px; /* Add margin to the left */
            text-decoration: none;
            width: 200px; /* Adjust width */
            height: 40px; /* Adjust height */
        }
        .category-button span {
            padding-left: 5px; /* Add padding to the text */
        }
        .category-button img {
            width: 25px;
            height: auto;
            margin-left: 5px;
        }
        </style>
    """
def load_normal_button_style():
    return """
        <style>
        a.button {
            background-color: #f0f2f6;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            color: #212121;
            padding: 8px 16px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }

        a.button:hover {
            background-color: #e0e0e0;
        }
        </style>
    """

def load_sidebar_styles_test():
    return """
        <style>

        div[data-testid="stPageLink-NavLink"] li div a {
            background-color: rgba(151, 166, 195, 0.15);
        }
   
        </style>
        """