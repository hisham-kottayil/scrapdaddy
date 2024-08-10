import streamlit as st
from pages.styles import load_sidebar_styles
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras




if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = ''
if 'authenticator_object' not in st.session_state:
    st.session_state['authenticator_object'] = '' 
authentication_status = st.session_state['authentication_status']
authenticator = st.session_state['authenticator_object']

hide_pages_dynamically(authentication_status)
hide_pages_extras()
if authentication_status and authentication_status != '':
    authenticator.logout('Logout!', 'sidebar', key = '1')
st.title("About Us!")
    # Inject the CSS into the Streamlit app
st.markdown(image_css, unsafe_allow_html=True)
st.markdown(load_sidebar_styles(), unsafe_allow_html=True)

# Display the clickable image in the sidebar
st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)