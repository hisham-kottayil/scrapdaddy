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

    # Your existing code...

    # Define your CSS for the horizontal colored strip
    strip_css = """
    <style>
    .enviro-section {
        position: relative;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        background-color: #f7f7f7;
        padding: 50px;
    }
    .enviro-section::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 50px; /* Height of the colored strip */
        background-color: #3498db; /* Color of the strip */
        z-index: -1; /* Place the strip behind the content */
    }
    .enviro-section h1 {
        font-size: 40px;
        color: #2e7d32;
        margin-bottom: 40px;
        position: relative; /* Make sure content is above the strip */
    }
    .enviro-section ul {
        list-style-type: none;
        padding: 0;
        font-size: 20px;
        color: #555;
    }
    .enviro-section ul li {
        margin-bottom: 20px;
    }
    .enviro-section.active {
        background-color: #d4edda !important;
    }
    </style>
    """

    st.markdown(strip_css, unsafe_allow_html=True)

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

    # The Enviro Mission section
    st.markdown("<div class='enviro-section' id='enviro-section'>", unsafe_allow_html=True)
    st.markdown("<h1>The Enviro Mission</h1>", unsafe_allow_html=True)
    st.markdown("<ul><li>Sustainable</li><li>Zero Waste</li><li>Fair Trade</li></ul>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # JavaScript to handle the scroll-triggered transition
    st.markdown(
        """
        <script>
        window.addEventListener('scroll', function() {
            const enviroSection = document.getElementById('enviro-section');
            const scrollY = window.scrollY;
            const triggerPoint = 300; // Adjust this value to control when the transition starts
            
            console.log('Scroll event triggered', scrollY); // Debugging line
            if (scrollY > triggerPoint) {
                enviroSection.style.opacity = '1';
                enviroSection.classList.add('active');
            } else {
                enviroSection.style.opacity = '0';
                enviroSection.classList.remove('active');
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()