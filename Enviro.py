import streamlit as st
import base64
from st_pages import Page, add_page_title, hide_pages
import time
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo, sustainable_logo_path, recyclable_logo_path, zero_waste_logo_path, home_page_icon
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
                            .mission-section {{
                                background-color: rgba(178, 210, 129, 0.3); /* Light green background */
                                width: 100%;
                                margin: 0;
                                padding: 50px 0; /* Padding to add space within the section */
                                text-align: center;
                            }}
                            .mission-section h2 {{
                                font-size: 36px;
                                color: #2a5d2b; /* Dark green */
                                margin-bottom: 20px;
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

    st.markdown(
        """
        <style>
        .container-box {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
            padding: 20px;
            width: 300px;
            height: 250px;
            border-radius: 8px;
            background-color: #daf7f1;
            text-align: center;
            margin: 0 auto;
        }
        .container-box h2 {
            margin-bottom: 18px;
            font-size: 25px;
            color: #422c17;
        }
        .category-button {{
            display: block;
            padding: 10px;
            text-decoration: none;
            color: #422c17;
            font-size: 20px;
        }}
        .category-button:hover {{
            background-color: #d2e8e3;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the container with category buttons
    for _ in range(12):
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
    img_html = f"""
    <div style="
        width: 100%;
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
    ">
        <img src="data:image/png;base64,{home_page_icon_base64}" style="
            width: 2000px;
            height: auto;
            object-fit: cover;
        " alt="Home Page Icon">
    </div>
    """

    with img_col:
        st.markdown(img_html, unsafe_allow_html=True)

    for _ in range(12):
        st.write("")
        
    # Define the paths to the logos
    sustainable_logo = f"data:image/png;base64,{load_image(sustainable_logo_path)}"
    zero_waste_logo = f"data:image/png;base64,{load_image(zero_waste_logo_path)}"
    recyclable_logo = f"data:image/png;base64,{load_image(recyclable_logo_path)}"

    # New section for "The Enviro Mission"
    mission_html = f"""
        <div class="scroll-section">
            <div class="mission-section">
                <h2>The Enviro Mission</h2>
                <p class="mission-paragraph">At Enviro, you can sell us your recyclable waste to help reduce landfill and conserve resources. Together, we can create a greener future.</p>
                <div class="mission-items">
                    <div class="mission-item">
                        <img src="{sustainable_logo}" alt="Sustainable" class="mission-logo">
                        <p>Sustainable</p>
                    </div>
                    <div class="mission-item">
                        <img src="{zero_waste_logo}" alt="Zero Waste" class="mission-logo">
                        <p>Zero Waste</p>
                    </div>
                    <div class="mission-item">
                        <img src="{recyclable_logo}" alt="Recyclable" class="mission-logo">
                        <p>Recyclable</p>
                    </div>
                </div>
            </div>
        </div>
        <style>
            .mission-items {{
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin-top: 20px;
            }}
            .mission-item {{
                text-align: center;
                width: 200px;
            }}
            .mission-logo {{
                width: 100px;
                height: 100px;
                margin-bottom: 10px;
            }}
            .mission-item p {{
                font-size: 24px;
                color: #2a5d2b;
            }}
            .mission-paragraph {{
                font-size: 20px;
                color: #2a5d2b;
                margin-left: 100px;
                margin-right: 100px;
                padding: 0 20px; /* Adds padding to the left and right */
            }}
        </style>
    """

    st.markdown(mission_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()