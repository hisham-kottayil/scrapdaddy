import streamlit as st
import base64
from st_pages import Page, add_page_title, hide_pages
import time
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo, sustainable_logo_path, recyclable_logo_path, zero_waste_logo_path, home_page_icon, signup_logo_path, materials_logo_path, pickup_logo_path, money_logo_path, home_font_path
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles, services_html, hiw_html, why_choose_us, mission_html, category_html, about_us_html
from dotenv import load_dotenv
import os
from pathlib import Path
from streamlit_navigation_bar import st_navbar




# Load the font file
def load_font(file_path):
    with open(file_path, "rb") as font_file:
        font_data = font_file.read()
    return base64.b64encode(font_data).decode('utf-8')


def main():
    st.set_page_config(layout="wide")
    
    # Define the path to the font file
    font_path = Path(home_font_path)

    # Get the base64 encoded font
    font_base64 = load_font(font_path)

    # Define CSS to use the custom font
    font_css = f"""
    <style>
    @font-face {{
    font-family: 'CustomFont';
    src: url('data:font/ttf;base64,{font_base64}') format('truetype');
    }}
    html, body, [class*="css"], .stApp, .stText, .stTitle, .stHeader, .stSubheader, .stMarkdown {{
    font-family: 'CustomFont', sans-serif;
    margin: 0;
    padding: 0;
    }}
    .container-box h2 {{
        font-family: 'CustomFont', sans-serif;
    }}

    .category-button span {{
        font-family: 'CustomFont', sans-serif;
    }}
    </style>
    """

    # Apply the custom font
    st.markdown(font_css, unsafe_allow_html=True)

    # Initialization
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 

    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']

    hide_pages_dynamically(authentication_status)
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)

    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key='1')

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
                                scroll-behavior: smooth;
                            }}
                            .css-1v3fvcr {{
                                background: none;
                            }}
                            .css-12ttj6m {{
                                background: none;
                            }}
                            .scroll-section {{
                                padding: 0;
                                margin: 0;
                                transition: background-color 1s ease;
                            }}
                        </style>
                        """

    st.markdown(background_style, unsafe_allow_html=True)
    
    # Existing content
    st.markdown(load_home_button_styles(), unsafe_allow_html=True)
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)

    st.markdown(image_css, unsafe_allow_html=True)

    def generate_logo_html(label, logo_path):
        logo_img_tag = f"<img src='data:image/png;base64,{load_image(logo_path)}' alt='{label} logo'>" if logo_path else ""
        return logo_img_tag

    st.markdown(category_html(), unsafe_allow_html=True)

    # Create the container with category buttons
    for _ in range(10):
        st.write("")

    empty_col, img_col = st.columns([1, 1.5])

    categories = ['Individual', 'Enterprises']

    container_html = '<div class="container-box">'
    container_html += '<h2>Choose Category</h2>'
    for cat in categories:
        link = "/Login"
        logo_img_tag = generate_logo_html(cat, logo_path=category_logos[cat])
        container_html += f'<a href="{link}" target="_self" class="category-button">{logo_img_tag} <span>{cat}</span></a>'
    container_html += '</div>'

    with empty_col:
        st.markdown(container_html, unsafe_allow_html=True)

    # Add image to the right column
    home_page_icon_base64 = load_image(home_page_icon)

    for _ in range(4):
        st.write("")
        
    about_us_str = about_us_html()

    st.markdown(about_us_str, unsafe_allow_html=True)

    for _ in range(2):
        st.write("")
    # New section for "Our Services"
    services_html_str = services_html()

    st.markdown(services_html_str, unsafe_allow_html=True)

    for _ in range(2):
        st.write("")

    signup_logo = f"data:image/png;base64,{load_image(signup_logo_path)}"
    materials_logo = f"data:image/png;base64,{load_image(materials_logo_path)}"
    pickup_logo = f"data:image/png;base64,{load_image(pickup_logo_path)}"
    money_logo = f"data:image/png;base64,{load_image(money_logo_path)}"
    

    # New section for "The Enviro Mission"
    hiw_html_str = hiw_html(signup_logo, materials_logo, pickup_logo, money_logo)

    st.markdown(hiw_html_str, unsafe_allow_html=True)

    # Additional section for "Why Choose Us?"
    why_choose_us_str = why_choose_us()

    st.markdown(why_choose_us_str, unsafe_allow_html=True)
    for _ in range(2):
        st.write("")
    # Define the paths to the logos
    sustainable_logo = f"data:image/png;base64,{load_image(sustainable_logo_path)}"
    zero_waste_logo = f"data:image/png;base64,{load_image(zero_waste_logo_path)}"
    recyclable_logo = f"data:image/png;base64,{load_image(recyclable_logo_path)}"

    # New section for "The Enviro Mission"
    mission_html_str = mission_html(sustainable_logo, zero_waste_logo, recyclable_logo)

    st.markdown(mission_html_str, unsafe_allow_html=True)
    



if __name__ == "__main__":
    main()