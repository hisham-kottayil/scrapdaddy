import streamlit as st
import base64
from st_pages import Page, show_pages, add_page_title, hide_pages
from pages.styles import load_sidebar_styles, load_home_button_styles
import time
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically
from dotenv import load_dotenv
import os

# Optional -- adds the title and icon to the current page
# add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be

show_pages(
    [
        Page("scrapdaddy_2.py", "Home"),
        Page("pages/login.py", "Login"),
        Page("pages/signup.py", "Sign Up"),
        Page("pages/materials.py", "Materials"),
        Page("pages/vehicles.py", "Vehicle"),
        Page("pages/address.py", "Address"),
        Page("pages/checkout.py", "Checkout"),
        Page("pages/orders.py", "My Orders"),
        Page("pages/about.py", "About us"),
    ]
)

def main():

    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 
        
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    
    hide_pages_dynamically(authentication_status)
    # st.set_page_config(initial_sidebar_state="collapsed")
    # page = st_navbar(["ScrapDaddy"])

    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)


    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 
        
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']

    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key='1')

    # Initialize session state for page
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'


    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False


    # Function to load images and encode them to base64
    def load_image(image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        return encoded_image

    # Encode the background image
    background_image = load_image(background_image_path)

    background_style = f"""
                        <style>
                            .stApp {{
                                background-image: url("data:image/png;base64,{background_image}");
                                background-size: cover;
                                background-repeat: no-repeat;
                                opacity: 0.99;
                            }}
                            .css-1v3fvcr {{
                                background: none;
                            }}
                            .css-12ttj6m {{
                                background: none;
                            }}
                        </style>
                        """

    st.markdown(background_style, unsafe_allow_html=True)
    # st.markdown(custom_font_css, unsafe_allow_html=True)
    empty_col, col = st.columns([ 1, 1])  # Adjust ratio to move the elements to the right


    # Add custom CSS to style the buttons
    st.markdown(load_home_button_styles(), unsafe_allow_html=True)
    # Add custom CSS to style the sidebar
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)



    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)

    # Display the clickable image in the sidebar



    def load_image(image_path):
        import base64
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    def generate_button_html(label, logo_path, link):
        logo_img_tag = f"<img src='data:image/png;base64,{load_image(logo_path)}' alt='{label} logo'>" if logo_path else ""
        return f"""
            <a href="{link}" target="_self" class="category-button">{label} {logo_img_tag}</a>
        """

    # Create empty rows for spacing
    for _ in range(18):
        st.write("")

    # Adjust columns to move the buttons to the right
    empty_col, col = st.columns([0.0001, 1])

    categories = ['Individual', 'Enterprises']

    # Generate HTML buttons
    with empty_col:
        for cat in categories:
            logo_path = category_logos[cat]
            link = f"/Login"
            button_html = generate_button_html(cat, logo_path, link)
            with col:
                st.markdown(button_html, unsafe_allow_html=True)


if __name__ == "__main__":
    
    main()