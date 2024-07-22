import streamlit as st
import base64
import streamlit.components.v1 as components
from datetime import date, datetime
from pages.styles import load_sidebar_styles
from constants import vehicles, limits, vehicle_logos
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo



def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image
# Function to handle the Vehicle page
def main():
    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)
    st.markdown(image_css, unsafe_allow_html=True)
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)

    st.subheader('Choose your vehicle')

    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = '' 

    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']

    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key='1')

    if not authentication_status:
        st.switch_page('scrapdaddy_2.py')

    def ChangeButtonAppearance(widget_label, logo_path=None, max_limit=None, selected=False):
        tick_mark = "✔️" if selected else ""
        logo_img_tag = f"<img src='data:image/png;base64,{load_image(logo_path)}' alt='{widget_label} logo' style='width: 50px; height: auto; margin-right: 5px;'>" if logo_path else ""
        limit_text = f"&nbsp;<span style='color: grey;'>(max: {max_limit} kgs)</span>" if max_limit else ""
        htmlstr = f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText.includes('{widget_label}')) {{ 
                        elements[i].style.fontSize = '15px';
                        elements[i].style.padding = '10px 65px';
                        elements[i].style.whiteSpace = 'nowrap';
                        elements[i].style.display = 'flex';
                        elements[i].style.alignItems = 'center';
                        elements[i].innerHTML = `{logo_img_tag} {widget_label} {limit_text} {tick_mark}`;
                    }}
                }}
            </script>
        """
        components.html(f"{htmlstr}", height=0, width=0)

    # Layout in 2x2 grid
    cols = st.columns(2)
    selected = st.session_state.get('selected_vehicle', None)
    
    for i, vehicle in enumerate(vehicles):
        logo_path = vehicle_logos[vehicle]
        max_limit = limits[vehicle]
        ChangeButtonAppearance(vehicle, logo_path, max_limit, selected == vehicle)
        
        button_html = f"""
            <button class="vehicle-button" onclick="window.location.href='/?vehicle={vehicle}'" style="display: flex; align-items: center; justify-content: center; white-space: nowrap;">
                <img src="data:image/png;base64,{load_image(logo_path)}" alt="{vehicle} logo" style="width: 50px; height: auto; margin-right: 5px;"/><br>
                {vehicle} <span style='color: grey;'>(max: {max_limit} kgs)</span> {"✔️" if selected == vehicle else ""}
            </button>
        """
        with cols[i % 2]:
            if st.button(button_html, key=f"{vehicle}_button"):
                selected = vehicle
                st.session_state['selected_vehicle'] = vehicle

    if selected:
        st.markdown(
            f'<span style="color:gray;">Vehicle: {selected}, maximum load: {limits[selected]} kgs ✔️</span>',
            unsafe_allow_html=True
        )

    st.subheader('Please choose preferred slot')
    today = date.today()
    date_chosen = st.date_input('Choose preferred Date', min_value=today)
    option = st.selectbox(
        'Time slot',
        ('7 AM - 11 AM', '11 AM - 4 PM', '4 PM - 7 PM'),
        placeholder='7 AM - 11 AM'
    )

    if st.button('Proceed to Add Address'):
        st.session_state.page = 'Address'
        st.switch_page("pages/address.py")

if __name__ == "__main__":
    main()