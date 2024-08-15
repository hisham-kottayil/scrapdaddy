import streamlit as st
from st_pages import Page, add_page_title, hide_pages
import base64


def hide_pages_dynamically(authentication_status):
    if not authentication_status:
        # st.write("Here1")
        st.sidebar.page_link('Enviro.py', label='Enviro')
        st.sidebar.page_link('pages/2_Login.py', label='Login')
        st.sidebar.page_link('pages/3_Signup.py', label='Signup')
        # st.sidebar.page_link('pages/9_About.py', label='About')
        # hide_pages(
        #     ["3_Signup", "Signup", "signup", "4_Materials", "Vehicle", "Address", "Checkout", "Orders", "styles"]
        #     )
    else:
        # st.write('Here2')
        st.sidebar.page_link('Enviro.py', label='Enviro')
        st.sidebar.page_link('pages/2_Login.py', label='Login')
        st.sidebar.page_link('pages/3_Signup.py', label='Signup')
        st.sidebar.page_link('pages/4_Materials.py', label='Materials')
        st.sidebar.page_link('pages/5_Vehicles.py', label='Vehicles')
        st.sidebar.page_link('pages/6_Address.py', label='Address')
        st.sidebar.page_link('pages/7_Checkout.py', label='Checkout')
        st.sidebar.page_link('pages/8_Orders.py', label='Orders')
        # st.sidebar.page_link('pages/9_About.py', label='About')
    
def hide_pages_extras():
    hide_pages(
        ["styles", "Test"]
        )
    
def load_sidebar_styles():
    return """
        <style>
        div[data-testid="stSidebarNav"] li div a {
            margin-left: 1rem;
            padding: 0.5rem;
            width: 200px;
            font-color: #ffffff;
            border-radius: 0.25rem;
            background-color: rgba(218, 247, 241, 1);
            /* border: 1px solid lightgrey; */
        }

        div[data-testid="stPageLink-NavLink"] li div a {
            background-color: rgba(151, 166, 195, 0.15);
        }
        [data-testid="stSidebarContent"] {
            background-color: #f7f8fa;
            padding: 20px;
            border-radius: 10px;
            font-size: 16px;
        }
        [data-testid="stSidebarHeader"] {
        /* Add your desired styles here */
        padding: 20px;
        height: 100px;
        }      
        </style>
        """
        
def load_home_button_styles():
    return """
        <style>
        .category-button {
            display: flex;
            align-items: center;
            justify-content: center; /* Center the text and image */
            background-color: rgb(35, 172, 160);
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
            padding: 10px 20px;
            margin: 10px 0;
            font-size: 15px; /* Adjust font size */
            font-family: Arial, sans-serif;
            color: white !important;
            margin-left: 20px; /* Add margin to the left */
            text-decoration: none;
            width: 200px; /* Adjust width */
            height: 40px; /* Adjust height */
        }
        .category-button span {
            padding-left: 5px; /* Add padding to the text */
        }
        .category-button img {
            width: 25px;
            height: auto;
            margin-left: 5px;
        }
        </style>
    """
def load_normal_button_style():
    return """
        <style>
        a.button {
            background-color: #f0f2f6;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            color: #212121;
            padding: 8px 16px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }

        a.button:hover {
            background-color: #e0e0e0;
        }
        </style>
    """
    
def category_html():
    return """
        <style>
        .container-box {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
            padding: 20px;
            width: 300px;
            height: 250px;
            border-radius: 8px;
            background-color: #daf7f1;
            text-align: center;
            margin: 0 auto;
        }
        .container-box h2 {
            margin-bottom: 18px;
            font-size: 25px;
            color: #422c17;
        }
        .category-button {{
            display: block;
            padding: 10px;
            text-decoration: none;
            color: #422c17;
            font-size: 20px;
        }}
        .category-button:hover {{
            background-color: #d2e8e3;
        }}
        </style>
        """

def services_html():
    return """
        <div class="services-section">
            <h2>Our Services</h2>
            <div class="services-items">
                <div class="service-item">
                    <h3>Recycling and Waste Management</h3>
                    <p>Our comprehensive recycling services cater to both residential and commercial clients, ensuring that your waste is collected, processed, and transformed into reusable materials efficiently and responsibly.</p>
                </div>
                <div class="service-item">
                    <h3>Pickup and Drop-off Services</h3>
                    <p>Convenience is key. Schedule a pickup through our user-friendly app, or drop off your recyclable materials at one of our designated locations. We operate on your schedule, making recycling easier than ever.</p>
                </div>
                <div class="service-item">
                    <h3>Monetization of Scrap</h3>
                    <p>Why throw it away when you can get paid for it? We offer competitive rates for a wide range of recyclable materials, including metals, paper, and electronics. Turn your waste into wealth with our seamless process.</p>
                </div>
            </div>
        </div>
        <style>
            .services-section h2,
            .services-section h3,
            .services-section p {
                font-family: 'CustomFont', sans-serif; /* Apply custom font to h2, h3, and p */
            }
            .services-section {
                padding: 50px 0;
                background-color: #F7F8FA;
                text-align: center;
                border-radius: 15px;
            }
            .services-section h2 {
                font-size: 36px;
                color: #2a5d2b;
                margin-bottom: 20px;
            }
            .services-items {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
            }
            .service-item {
                background-color: #DBF7F1;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                padding: 20px;
                width: 30%;
                margin: 10px;
            }
            .service-item h3 {
                font-size: 24px;
                color: #422c17;
                margin-bottom: 10px;
            }
            .service-item p {
                font-size: 18px;
                color: #555555;
            }
        </style>
    """
    
def hiw_html(signup_logo, materials_logo, pickup_logo, money_logo):
    return f"""
        <div class="scroll-section">
            <div class="hiw-section">
                <h2>How it works?</h2>
                <div class="hiw-items">
                    <div class="hiw-item">
                        <img src="{signup_logo}" alt="Signup" class="hiw-logo">
                        <p>Signup</p>
                        <h7>Create an account in minutes through our website or app</h7>
                    </div>
                    <div class="hiw-item">
                        <img src="{materials_logo}" alt="Select Materials" class="hiw-logo">
                        <p>Select Materials</p>                        
                        <h7>Choose the types of materials you want to recycle to ensure proper processing</h7>
                    </div>
                    <div class="hiw-item">
                        <img src="{pickup_logo}" alt="Schedule Pickup" class="hiw-logo">
                        <p>Schedule Pickup</p>                        
                        <h7>Pick a date and time that suits you, and we'll handle the rest</h7>
                    </div>
                    <div class="hiw-item">
                        <img src="{money_logo}" alt="Get Paid" class="hiw-logo">
                        <p>Get Paid</p>                        
                        <h7>Receive payment directly to your account once your materials are processed</h7>
                    </div>
                </div>
            </div>
        </div>
        <style>
            .hiw-section, .hiw-item, .hiw-item p, .hiw-section h2, .hiw-item h7 {{
                font-family: 'CustomFont', sans-serif;
            }}

            .hiw-section {{
                background-color: #E8F1DA; /* Light green background */
                width: 100%;
                margin: 0;
                padding: 50px 0; /* Padding to add space within the section */
                text-align: center;
                border-radius: 15px; 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow to the section */
                border: 5px solid #F7F8FA; /* Thin border with color #F7F8FA */
            }}
            .hiw-section h2 {{
                font-size: 36px;
                color: #422c17; /* Dark green */
                margin-bottom: 20px;
            }}
            .hiw-section h7 {{
                color: #2a5d2b; /* Dark green */
            }}
            .hiw-items {{
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                align-items: center;
                margin-top: 20px;
            }}
            .hiw-item {{
                text-align: center;
                width: 45%;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow to each item */
                border-radius: 8px; /* Add rounded corners to items */
                padding: 20px; /* Add padding for better spacing */
                background-color: #fff; /* White background for better contrast with shadow */
            }}
            .hiw-logo {{
                width: 100px;
                height: 100px;
                margin-bottom: 10px;
            }}
            .hiw-item p {{
                font-size: 24px;
                color: #2a5d2b;
            }}
            .hiw-paragraph {{
                font-size: 20px;
                color: #2a5d2b;
                margin-left: 100px;
                margin-right: 100px;
                padding: 0 20px; /* Adds padding to the left and right */
            }}
        </style>
    """
    
def why_choose_us():
    return """
         <div class="why-choose-us-section">
            <h2>Why Choose Us?</h2>
            <div class="why-choose-us-items">
                <div class="why-choose-us-item">
                    <h3>Eco-Friendly Approach</h3>
                    <p>We prioritize sustainability in everything we do, from the way we process waste to the materials we use in our operations.</p>
                </div>
                <div class="why-choose-us-item">
                    <h3>Competitive Rates</h3>
                    <p>Maximize your returns with our transparent pricing and fair market rates for all recyclable materials.</p>
                </div>
                <div class="why-choose-us-item">
                    <h3>Customer-Centric Service</h3>
                    <p>Our intuitive app and dedicated customer support team ensure that your recycling experience is hassle-free and rewarding.</p>
                </div>
                <div class="why-choose-us-item">
                    <h3>Community Impact</h3>
                    <p>By choosing us, you're contributing to a cleaner environment and a healthier community. Together, we can make a difference.</p>
                </div>
            </div>
        </div>
        <style>
            .why-choose-us-section, .why-choose-us-section h2, .why-choose-us-item h3, .why-choose-us-item p {
                font-family: 'CustomFont', sans-serif;
            }

            .why-choose-us-section {
                padding: 50px 0;
                background-color: #F7F8FA; /* Light green background */
                text-align: center;
                border-radius: 15px;
                margin-top: 30px;
            }
            .why-choose-us-section h2 {
                font-size: 36px;
                color: #2a5d2b;
                margin-bottom: 20px;
            }
            .why-choose-us-items {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
            }
            .why-choose-us-item {
                background-color: #E8F1DA;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                padding: 20px;
                width: 45%;
                margin: 10px;
                text-align: center; /* Center-aligns the text */
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            .why-choose-us-item h3 {
                font-size: 24px;
                color: #422c17;
                margin-bottom: 10px;
            }
            .why-choose-us-item p {
                font-size: 18px;
                color: #555555;
            }
        </style>   
    """
    
def mission_html(sustainable_logo, zero_waste_logo, recyclable_logo):
    return f"""
        <div class="scroll-section">
            <div class="mission-section">
                <h2>The Enviro Mission</h2>
                <p class="mission-paragraph">At Enviro, you can sell us your recyclable waste to help reduce landfill and conserve resources. Together, we can create a greener future.</p>
                <div class="mission-items">
                    <div class="mission-item">
                        <img src="{sustainable_logo}" alt="Sustainable" class="mission-logo">
                        <p>Sustainable</p>
                    </div>
                    <div class="mission-item">
                        <img src="{zero_waste_logo}" alt="Zero Waste" class="mission-logo">
                        <p>Zero Waste</p>
                    </div>
                    <div class="mission-item">
                        <img src="{recyclable_logo}" alt="Recyclable" class="mission-logo">
                        <p>Recyclable</p>
                    </div>
                </div>
            </div>
        </div>
        <style>
            .mission-section, .mission-section h2, .mission-item p, .mission-paragraph {{
                font-family: 'CustomFont', sans-serif;
            }}

            .mission-section {{
                background-color: #E8F1DA; /* Light green background */
                width: 100%;
                margin: 0;
                padding: 50px 0; /* Padding to add space within the section */
                text-align: center;
                border-radius: 15px; 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow to the section */
                border: 5px solid #F7F8FA; /* Thin border with color #F7F8FA */

            }}
            .mission-section h2 {{
                font-size: 36px;
                color: #422c17; /* Dark brown */
                margin-bottom: 20px;
            }}
            .mission-items {{
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin-top: 20px;
            }}
            .mission-item {{
                text-align: center;
                width: 200px;
            }}
            .mission-logo {{
                width: 100px;
                height: 100px;
                margin-bottom: 10px;
            }}
            .mission-item p {{
                font-size: 20px;
                color: #422c17;
            }}
            .mission-paragraph {{
                font-size: 20px;
                color: #422c17;
                margin-left: 100px;
                margin-right: 100px;
                padding: 0 20px; /* Adds padding to the left and right */
            }}
        </style>
    """

def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image
