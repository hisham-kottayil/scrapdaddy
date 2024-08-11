import streamlit as st
import base64
from st_pages import Page, add_page_title, hide_pages
import time
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles
from dotenv import load_dotenv
import os



def main():
    st.set_page_config(layout="wide")

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
                                scroll-behavior: smooth;
                            }}
                            .background-section {{
                                background-image: url("data:image/png;base64,{background_image}");
                                background-size: cover;
                                background-repeat: no-repeat;
                                background-attachment: fixed; /* Creates parallax effect */
                                height: 100vh; /* Full viewport height */
                                display: flex;
                                justify-content: center;
                                align-items: center;
                            }}
                            .scroll-section {{
                                padding: 0;
                                margin: 0;
                                transition: background-color 1s ease;
                            }}
                            .mission-wrapper {{
                                width: 100vw; /* Full viewport width */
                                margin: 0;
                                padding: 0;
                                background-color: #d0f4de; /* Light green background */
                                overflow: hidden; /* Ensure no horizontal scroll */
                            }}
                            .mission-section {{
                                padding: 50px 0; /* Padding to add space within the section */
                                text-align: center;
                            }}
                            .mission-section h2 {{
                                font-size: 36px;
                                color: #2a5d2b; /* Dark green */
                                margin-bottom: 20px;
                            }}
                            .mission-section ul {{
                                list-style-type: none;
                                padding: 0;
                                font-size: 24px;
                                color: #2a5d2b;
                            }}
                            .mission-section li {{
                                margin: 10px 0;
                            }}
                        </style>
                        """

    st.markdown(background_style, unsafe_allow_html=True)

    # First section with background image
    st.markdown(
        """
        <div class="background-section">
            <div>
                <h1 style="color: white;">Welcome to Our Homepage</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create the container with category buttons
    for _ in range(12):
        st.write("")

    empty_col, col = st.columns([1, 1.5])

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

    # New section for "The Enviro Mission"
    mission_html = """
    <div class="scroll-section">
        <div class="mission-wrapper">
            <div class="mission-section">
                <h2>The Enviro Mission</h2>
                <ul>
                    <li>Sustainable</li>
                    <li>Zero Waste</li>
                    <li>Recyclable</li>
                </ul>
            </div>
        </div>
    </div>
    """

    st.markdown(mission_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()