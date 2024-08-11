import streamlit as st
import requests
import streamlit_authenticator as stauth
from time import sleep
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles, load_normal_button_style
import time

def main():
    start  = time.time()
    # st.write('Here')
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = ''     
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    st.write(authentication_status)
    hide_pages_dynamically(authentication_status)
    # hide_pages_extras()
    # Function to fetch user data
    # @st.cache_data(ttl=3600)  # Cache for 1 hour

    secret_key = st.secrets['SECRET_KEY']
    api_url =  st.secrets['URL']
    header =  st.secrets['HEADER']
    
    def fetch_user_data(query):
        url = api_url
        headers = {header: secret_key}
        
        r = requests.post(url=url, json=query, headers=headers)
        r.raise_for_status()  # Raise an error for bad status codes
        return r.json()['data']

    # def login():
    st.title("Login/Logout")
    st.query_params['stay_in_login_page'] = True

    try:
        query = {
            "query": "query MyQuery { user { id name password email } }"
        }        
        # Fetch and cache user data
        data = fetch_user_data(query)

    except requests.RequestException as e:
        st.error(f"Failed to fetch user data: {e}")
        # return
    credentials = {
        "usernames": {}
    }

    for user in data["user"]:
        credentials["usernames"][user["name"]] = {
            "name": user["email"],
            "password": user["password"]
        }

    authenticator = stauth.Authenticate(credentials, "scrapdaddy_dashboard", "abcdef", cookie_expiry_days=1)

    # st.write(f'{time.time() - start} secs')

    st.query_params['authenticator_object'] = authenticator

    email, authentication_status, username = authenticator.login(fields = {'Form name':'Login', 'Username':'Username', 'Password':'Password', 'Login':'Login'})  #location = 'sidebar'
    st.query_params['authenticator_object'] = authenticator
    st.query_params['authentication_status'] = authentication_status

    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = authenticator
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = authentication_status

    if authentication_status == False:
        st.error("Username/password is incorrect")
        st.session_state['logged_in'] = False
        st.session_state.authentication_status = False


    if authentication_status == None:
        st.warning("Please enter your username and password")
        st.session_state['logged_in'] = False
        st.session_state.authentication_status = None


    if authentication_status:
        st.session_state['logged_in'] = True
        st.session_state.authentication_status = True
        st.session_state['authenticator_object'] = authenticator

        sleep(0.5)
        
        
        for i in range(len(data["user"])):
            if data["user"][i]["name"] == username:
                # st.write(data["user"][i])
                st.query_params['user_id'] = data["user"][i]["id"]
                st.query_params['user_name'] = data["user"][i]["name"]
                
                # st.write(st.query_params['user_id'])
        # authenticator.logout()
        st.write(f"Logged in successfully as {st.query_params['user_name']}!")
        authenticator.logout('Logout!', 'sidebar', key = '1')
        st.switch_page("pages/4_Materials.py")
        st.session_state.page = 'Material'

    # Add a signup button
    st.text("")
    st.text("")
    st.text("")
    # if st.button("Doesn't have an account? Sign Up!"):
    #     st.session_state.page = 'Sign Up'
        
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)

    # Include the CSS in your Streamlit app
    st.markdown(load_normal_button_style(), unsafe_allow_html=True)
    

    # Create a button using HTML
    st.markdown('<a href="/signup" target="_self" class="button">Does not have an account? Sign Up!</a>', unsafe_allow_html=True)

    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)
    # Display the clickable image in the sidebar
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)
    
# login()

if __name__ == "__main__":
    
    main()
