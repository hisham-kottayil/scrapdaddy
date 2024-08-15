import streamlit as st
import base64
import streamlit.components.v1 as components
from datetime import date, datetime
from constants import vehicles, limits, vehicle_logos
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles
import pytz


def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image
# Function to handle the Vehicle page
def main():
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)

    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)
    # Display the clickable image in the sidebar

    # st.write(st.session_state)

    st.title('Choose your preferred slot')
    today = date.today()
    date_chosen = st.date_input('Pickup Date', min_value = today)
    st.session_state['date_chosen'] = date_chosen
    
    saudi_tz = pytz.timezone('Asia/Riyadh')
    ist_tz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist_tz).time()
    current_hour = current_time.hour
    
    # Define the mapping of options to IDs
    options = {
        '7 AM - 11 AM': 1,
        '11 AM - 4 PM': 2,
        '4 PM - 7 PM': 3
    }

    # Create a list of option texts for the selectbox
    option_texts = list(options.keys())

    # Create the selectbox with the option texts
    option = st.selectbox(
        'Time slot',
        option_texts,
        index=option_texts.index('7 AM - 11 AM'),  # Default selection
        placeholder='7 AM - 11 AM'
    )
    # st.write(current_hour)
    # st.write(options[option])
    if date_chosen != today: 
        st.session_state['time_slot_validity'] = True
    else:
        if options[option] == 1 and current_hour > 11:
            st.error('Please choose a valid timeslot.')
            st.session_state['time_slot_validity'] = False
        elif options[option] == 2 and current_hour > 16:
            st.error('Please choose a valid timeslot.')
            st.session_state['time_slot_validity'] = False
        elif options[option] == 3 and current_hour > 19:
            st.error('Please choose a valid timeslot.')
            st.session_state['time_slot_validity'] = False
        else:
            st.session_state['time_slot_validity'] = True
    
    
    st.session_state['time_slot'] = option
    

    st.subheader('Choose your vehicle')
    
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 
        
    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    hide_pages_dynamically(authentication_status)
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)

    # hide_pages_extras()
    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key='1')

    if not authentication_status:
        st.switch_page('Enviro.py')


    def ChangeButtonAppearance(widget_label, logo_path=None, max_limit=None):
        logo_img_tag = f"<img src='data:image/png;base64,{load_image(logo_path)}' alt='{widget_label} logo' style='width: 50px; height: auto; margin-right: 5px;'>" if logo_path else ""
        limit_text = f"&nbsp;<span style='color: grey;'>(max: {max_limit} kgs)</span>" if max_limit else ""
        htmlstr = f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText.includes('{widget_label}')) {{ 
                        elements[i].style.fontSize = '15px';  // Adjust size as needed
                        elements[i].style.padding = '2px 65px';  // Adjust padding as needed
                        elements[i].style.whiteSpace = 'nowrap';  // Ensure text is in one line
                        elements[i].style.display = 'flex';
                        elements[i].style.alignItems = 'center';
                        elements[i].innerHTML = `{logo_img_tag} {widget_label}  {limit_text}`;
                    }}
                }}
            </script>
        """
        components.html(f"{htmlstr}", height=0, width=0)

    # Layout in 2x2 grid
    cols = st.columns(2)
    selected = {}
    for i, vehicle in enumerate(vehicles):
        logo_path = vehicle_logos[vehicle]
        max_limit = limits[vehicle]
        # ChangeButtonAppearance(vehicle, logo_path, max_limit)
        button_html = f"""
            <button class="vehicle-button" onclick="window.location.href='/?vehicle={vehicle}'" style="display: flex; align-items: center; justify-content: center; white-space: nowrap;">
                <img src="data:image/png;base64,{load_image(logo_path)}" alt="{vehicle} logo" style="width: 50px; height: auto; margin-right: 5px;"/><br>
                {vehicle} <span style='color: grey;'>(max: {max_limit} kgs)</span>
            </button>
        """
        with cols[i % 2]:
            selected_vehicle = st.button(button_html, key=f"{vehicle}_button")
            st.write('Here2')
            if selected_vehicle:
                selected = {}
                selected['vehicle'] = vehicle
        # st.write('here3')
    st.write('Here')
    if selected:
        st.session_state['selected_vehicle'] = selected["vehicle"]
        try:
            st.markdown(
                f'<span style="color:gray;">Vehicle: {selected["vehicle"]}, maximum load: {limits[selected["vehicle"]]} kgs ✔️</span>',
                unsafe_allow_html=True
            )
        except:
            pass

    if st.button('Proceed to Add Address'):
        if st.session_state['time_slot_validity'] == False:
            st.error('Please choose a valid timeslot.')
        else:
            st.session_state.page = 'Address'
            st.switch_page("pages/6_Address.py")
        

if __name__ == "__main__":
    main()