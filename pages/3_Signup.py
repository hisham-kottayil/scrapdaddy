import streamlit as st
import requests
from streamlit_authenticator.utilities.hasher import Hasher
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles


def signup():
    # Display signup form
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
    st.title("Sign Up")
    name = st.text_input("Enter Username")
    email = st.text_input("New Email")
    password = st.text_input("New Password", type='password')
    hashed_passwords = []
    
    secret_key = st.secrets['SECRET_KEY']
    api_url =  st.secrets['URL']
    header =  st.secrets['HEADER']
    
    # Check if the user clicked the "Sign Up" button
    if st.button("Sign Up"):
        if email == "" or password == "":
            st.error("Email and password are required.")
        else:
            hashed_passwords = Hasher([password]).generate()[0]

        url = api_url
        headers = {header: secret_key}

        mutation = """
        mutation InsertUser($name: String!, $password: String!, $email: String!) {
        insert_user(objects: {name: $name, password: $password, email: $email}) {
            affected_rows
        }
        }
        """

        variables = {
            "name": name,
            "password": hashed_passwords,
            "email": email
        }

        json_data = {
            "query": mutation,
            "variables": variables
        }

        # try:
        # r = requests.post(url=url, json=json_data, headers=headers)
        # r.raise_for_status()  # Check for HTTP request errors
        # response_data = r.json()
        # st.write(response_data)
        # st.write(r.raise_for_status())
        # # st.write(response_data)
        # if st.button("Successfully registered User. Please login to Continue!"):
        #     # st.session_state.page = 'Login'
        #     st.switch_page("pages/2_Login.py")
        # # except requests.exceptions.RequestException as e:
        # #     print(f"An error occurred: {e}")


        try:
            r = requests.post(url=url, json=json_data, headers=headers)
            r.raise_for_status()  # Check for HTTP request errors

            response_data = r.json()
            if "errors" in response_data:
                # error_message = response_data["errors"][0]["message"]
                # error_code = response_data["errors"][0]["extensions"]["code"]
                st.write(response_data)
                st.error(f"Email already exists! Please use a different email or log in.")
                # st.write(f"Error Code: {error_code}")
            else:
                st.success(f"Successfully registered User. Please login to Continue!")
                # if st.button("Login"):
                #     st.switch_page("pages/2_Login.py")
                # if st.button("Successfully registered User. Please login to Continue!"):
                #     # st.session_state.page = 'Login'
                #     st.switch_page("pages/2_Login.py")
        except Exception as err:
            st.write(f"Error occurred: {err}")
            
signup()
