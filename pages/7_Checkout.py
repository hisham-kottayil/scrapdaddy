import streamlit as st
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo, limits
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles
import requests

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
    st.subheader('Vehicle Choosen')
    # st.write(st.session_state['selected_vehicle'])
    if 'selected_vehicle' in st.session_state.keys():
        st.write(f"{st.session_state['selected_vehicle']} - max weight: {limits[st.session_state['selected_vehicle']]} kgs")
        # st.write(limits[st.session_state['selected_vehicle']])
    else:
        st.write('Please choose a vehicle')
    st.subheader('Customer Details')
    # if 'addess' in st.session_state.keys():
    #     st.write(st.session_state['addess'])
    # else:
    #     st.write('Please add address')
    if 'customer_details' in st.session_state.keys():
        st.write(st.session_state['customer_details'])
    else:
        st.write('Please add customer details')
    st.subheader('Pickup Slot')
    if 'date_chosen' in st.session_state.keys():
        st.write(f'date chosen: {st.session_state['date_chosen']}')
    if 'time_slot' in st.session_state.keys():
        st.write(f'time slot chosen: {st.session_state['time_slot']}')
    # Add a checkout button
    # st.button('Checkout')
    col1, col2, col3 = st.columns(3)
    with col3:
        if st.button('Schedule'):
            if 'selected_vehicle' not in st.session_state.keys():
                st.error("Please choose vehicle to proceed.")
            elif 'address' not in st.session_state.keys():
                st.error("Please add address to proceed.")
            elif 'date_chosen' not in st.session_state.keys():
                st.error("Please choose pickup date to proceed.")
            elif 'time_slot' not in st.session_state.keys():
                st.error("Please chose time slot to proceed.")
            # if ('address' in st.session_state.keys()) and ('selected_vehicle' in st.session_state.keys()):
            else:
                with st.spinner('Scheduling. Please wait a moment...'):
                    try:
                        secret_key = st.secrets['SECRET_KEY']
                        api_url = st.secrets['URL']
                        header = st.secrets['HEADER']

                        mutation = """
                        mutation InsertOrder($address_id: Int!, $user_id: Int!, $is_completed: Boolean!) {
                        insert_order(objects: {address_id: $address_id, user_id: $user_id, is_completed: $is_completed}) {
                            affected_rows
                        }
                        }
                        """

                        url = api_url
                        headers = {header: secret_key}

                        # Define the variables to pass to the mutation
                        variables = {
                            'address_id': 1,
                            'user_id': st.session_state['user_id'],
                            'is_completed': False
                        }

                        json_data = {
                            "query": mutation,
                            "variables": variables
                        }

                        r = requests.post(url=url, json=json_data, headers=headers)
                        r.raise_for_status()  # Check for HTTP request errors
                        response_data = r.json()
                        if "errors" in response_data:
                            st.error('Error occured while scheduling the pickup. Please contact the team')
                        else:
                            st.success('Pickup scheduled! Go to Orders page to view the status.')
                    except Exception as err:
                        st.write(f"Error occurred: {err}")

                
if __name__ == "__main__":
    main()