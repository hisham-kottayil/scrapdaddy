import streamlit as st
from pages.styles import load_sidebar_styles
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo


def main():

    # st.write(st.session_state)
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
        st.write(st.session_state['addess'])
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