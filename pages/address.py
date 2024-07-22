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
        st.switch_page('scrapdaddy_2.py')
    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key = '1')
    # Input fields for address information
    name = st.text_input('Name')
    contact = st.text_input('Contact')
    house_number = st.text_input('House Number')
    city = st.text_input('City')
    state = st.text_input('State')
    pincode = st.text_input('Pincode')




    st.markdown(
        """
        <style>
        .mandatory::after {
            content: '*';
            color: red;
            padding-left: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Labels with red asterisks
    st.markdown('<label class="mandatory">Name</label>', unsafe_allow_html=True)
    name = st.text_input("", max_chars=50)

    st.markdown('<label class="mandatory">Contact</label>', unsafe_allow_html=True)
    contact = st.text_input("", max_chars=15)
    
    st.markdown("**Address**")
    address = st.text_area("")

    if st.button("Submit"):
        if not name:
            st.error("Name is required.")
        elif not contact:
            st.error("Contact is required.")
        elif not contact.isdigit():
            st.error("Contact must contain only numbers.")
        else:
            st.success("Form submitted successfully!")
            st.write("Name:", name)
            st.write("Contact:", contact)
            st.write("Address:", address)
            
            

    # Display the entered information
    if st.button('Proceed'):
        st.session_state['addess'] = f"""
        Name: {name}\n
        Contact Number: {contact}\n
        Address: {house_number}, {city}, {state}, {pincode}
        """
        st.session_state.page = 'Checkout'
        st.switch_page("pages/checkout.py")

if __name__ == "__main__":
    main()