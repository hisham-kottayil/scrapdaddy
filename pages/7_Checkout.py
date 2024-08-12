import streamlit as st
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles

def main():

    # st.write(st.session_state)
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
    st.title('Confirm Your Order')
    st.write("")
    st.write("")
    st.write("")
    st.subheader('Vehicle Choosen')
    if 'selected_vehicle' in st.session_state.keys():
        st.write(st.session_state['selected_vehicle'])
    else:
        st.write('Please choose a vehicle')
    st.write("")
    st.subheader('Pickup Address')
    if 'addess' in st.session_state.keys():
        # st.write(st.session_state['addess'])
        pass
    else:
        st.write('Please add address')
    st.write("")
    st.write("")
    st.write("")
    # Add a checkout button
    # st.button('Checkout')
    col1, col2, col3 = st.columns(3)
    with col3:
        if st.button('Checkout'):
            if 'selected_vehicle' not in st.session_state.keys():
                st.error("Please choose vehicle to proceed.")
            if 'addess' not in st.session_state.keys():
                st.error("Please add address to proceed.")
            if ('addess' in st.session_state.keys()) and ('selected_vehicle' in st.session_state.keys()):
                st.success('Pickup scheduled!')
                # st.switch_page("pages/orders.py")
            
                
if __name__ == "__main__":
    main()