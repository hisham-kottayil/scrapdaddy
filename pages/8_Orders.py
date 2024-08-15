import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from dotenv import load_dotenv
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles

secret_key = st.secrets['SECRET_KEY']
api_url =  st.secrets['URL']
header =  st.secrets['HEADER']

# Function to fetch user data
# @st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_user_data(query):

    url = api_url
    headers = {header: secret_key}
    
    r = requests.post(url=url, json=query, headers=headers)
    r.raise_for_status()  # Raise an error for bad status codes
    return r.json()['data']



def get_bill(order_id):
    st.subheader("Bill")
    query = {
        "query": f"""
            query MyQuery {{
            bill(where: {{order_id: {{_eq: {order_id} }}}}) {{
                order_id
                material {{
                material_name
                }}
                quantity
                price
            }}
            }}
            """
    }
    data = fetch_user_data(query)
    # Extracting the relevant data from JSON into a list of dictionaries
    rows = []
    for item in data["bill"]:
        row = {
            "material": item["material"]["material_name"],
            "quantity": item["quantity"],
            "price": item["price"]
        }
        rows.append(row)

    # Creating a DataFrame
    df = pd.DataFrame(rows)

    # Adding the material_name column (just for clarity)
    df["material_name"] = df["material"]

    # Reordering columns as required
    df = df[["material", "quantity", "price"]]
    total_price = df["price"].sum(skipna=True)

    st.write(df)
    st.write(f"Total price: Rs.{total_price}")
    
def main():
    st.title("Orders")

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
    user_id = st.query_params['user_id']
    st.write(user_id)
    # user_id = 94
    query = {
        "query": f"""
            query MyQuery {{
            user(where: {{id: {{_eq: {int(user_id)} }}}}) {{
                orders(order_by: {{id: desc}}) {{

                id
                is_completed
                created_at
                }}
            }}
            }}
            """
    }
    data = fetch_user_data(query)

    # Extract the orders
    orders = data["user"][0]["orders"]
    st.markdown(
        """
        <style>
        .order-box {
            border: 1px solid #000;
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            box-sizing: border-box;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    status_map = {
        'True': 'Completed',
        'False': 'Pending'
    }

    st.markdown( """
    <style>
    /* Style for the form */
    [data-testid="stForm"] {
        background-color: rgb(218, 247, 241); /* Alice green background color */
    }
    </style>
    """,
        unsafe_allow_html=True
    )


    for order in orders:
        dt = datetime.fromisoformat(order['created_at'].split('+')[0])

        # Extract just the date
        date_only = dt.date()

        button_html = ""
        if order['is_completed']:
            with st.form(key=f"form_{order['id']}"):
                st.markdown(
                    f"""
                    <div class="order-box">
                        <div>
                            Order ID: {order['id']}<br>
                            Date: {date_only}<br>
                            Status: {status_map[str(order['is_completed'])]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                submitted = st.form_submit_button(label='Get Bill')
                if submitted:
                    get_bill(order['id'])
        else:
            st.markdown(
                f"""
                <div class="order-box">
                    <div>
                        Order ID: {order['id']}<br>
                        Date: {date_only}<br>
                        Status: {status_map[str(order['is_completed'])]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            
if __name__ == "__main__":
    main()
