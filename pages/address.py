import streamlit as st
from pages.styles import load_sidebar_styles
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo


# Function to handle the Address page
def main():
    
    # st.write(st.session_state)
    st.title('Address Information Form')
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)
    
    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)
    # Display the clickable image in the sidebar
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)
    
    
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 
        
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    if not authentication_status:
        st.switch_page('Enviro.py')
    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key = '1')
    # Input fields for address information
    name = st.text_input('Name')
    contact = st.text_input('Contact')
    # house_number = st.text_input('House Number')
    address = st.text_area('Address')
    region = st.text_input('Region')
    district = st.text_input('District')
    pincode = st.text_input('Pincode')



    # Display the entered information
    if st.button('Proceed'):
        st.session_state['addess'] = f"""
        Name: {name}\n
        Contact Number: {contact}\n
        Address: {address}, {region}, {district}, {pincode}
        """
        st.session_state.page = 'Checkout'
        st.switch_page("pages/Checkout.py")

if __name__ == "__main__":
    main()