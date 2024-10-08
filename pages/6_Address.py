import streamlit as st
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles

# Function to handle the Address page
def main():
    
    # st.write(st.session_state)
    st.title('Address Information Form')
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)
    
    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)
    # Display the clickable image in the sidebar
    
    
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 
        
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    hide_pages_dynamically(authentication_status)
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)

    # hide_pages_extras()
    if not authentication_status:
        st.switch_page('Enviro.py')
    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key = '1')
    # Input fields for address information
    name = st.text_input('Name', placeholder = 'Mandatory')
    contact = st.number_input('Contact', value = None, format="%0.0f", step = None, placeholder = 'Mandatory')  # Empty label for the actual input field
    # house_number = st.text_input('House Number')
    address = st.text_area('Address', placeholder = 'Mandatory')
    region = st.text_input('Region')
    pincode = st.text_input('Pincode', placeholder = 'Mandatory')


    contact = int(contact) if contact else ''
    # Display the entered information
    if st.button('Proceed'):
        if contact == '' or name == '' or address == '' or pincode == '':
            st.error("Please provide all the mandatory fields to proceed.")
        else:
            st.session_state['address'] = f"""
            Name: {name}\n
            Contact Number: {contact}\n
            Address: {address}\n
            Region: {region}, {pincode}
            """
            st.session_state['customer_details'] = f"""
            Name: {name}\n
            Contact Number: {contact}
            """
            st.session_state.page = 'Checkout'
            st.switch_page("pages/7_Checkout.py")

if __name__ == "__main__":
    main()