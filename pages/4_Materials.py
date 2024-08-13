import streamlit as st
from st_pages import Page, add_page_title
from constants import background_image_path, category_logos, clickable_image, link_url, image_css, logo
from helper import hide_pages_dynamically, hide_pages_extras, load_sidebar_styles, load_home_button_styles

def navigate(url):
    st.components.v1.html(f"""
        <script>
            window.location.href = '{url}';
        </script>
    """)
    
def load_image(image_path):
    import base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def generate_button_html(label, logo_path, link):
    logo_img_tag = f"<img src='data:image/png;base64,{load_image(logo_path)}' alt='{label} logo'>" if logo_path else ""
    return f"""
        <a href="{link}" target="_self" class="category-button">{label} {logo_img_tag}</a>
    """

def main():

    st.markdown(load_sidebar_styles(), unsafe_allow_html=True)

    # Inject the CSS into the Streamlit app
    st.markdown(image_css, unsafe_allow_html=True)
    # Display the clickable image in the sidebar

    # st.write(st.session_state)
    # def material_page():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = ''
    if 'authenticator_object' not in st.session_state:
        st.session_state['authenticator_object'] = ''

    st.markdown('### <span style="font-size:40px;font-weight:bold;">Choose material(s)</span> - <span style="color:grey; font-size:32px;">optional</span>', unsafe_allow_html=True)

    authentication_status = st.session_state['authentication_status']
    authenticator = st.session_state['authenticator_object']
    hide_pages_dynamically(authentication_status)
    st.sidebar.markdown(clickable_image(logo, link_url, width=150, height=150), unsafe_allow_html=True)

    # hide_pages_extras()
    if not authentication_status:
        st.switch_page('Enviro.py')

    if authentication_status and authenticator != '':
        authenticator.logout('Logout!', 'sidebar', key = '1')

    if 'selected_materials' not in st.session_state:
        st.session_state.selected_materials = set()

    # Create checkboxes
    materials = ['Paper', 'Wood', 'Copper', 'Aluminium', 'Cardboard', 'Plastic', 'Other Metals']
    prices = {
        'Metal': 'Rs.100/kg', 'Paper': 'Rs.10/kg', 'Wood': 'Rs.50/kg', 'Copper': 'Rs.50/kg',
        'Aluminium': 'Rs.50/kg', 'Cardboard': 'Rs.50/kg',  'Plastic': 'Rs.50/kg',  'Other Metals': 'Rs.50/kg'
        }

    for material in materials:
        # Check if the material is selected
        is_selected = material in st.session_state.selected_materials
        
        # Style for selected and unselected states
        div_style = f"""
            <div style="
                border: 2px solid grey;
                border-radius: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px;
                margin: 5px 0;
                background-color: {'blue' if is_selected else 'white'};
                color: {'white' if is_selected else 'black'};
            ">
                <span>{material} <small style="font-size: 0.8em; color: grey;">({prices[material]})</small></span>
                <input type="checkbox" id="{material}" {'checked' if is_selected else ''} onclick="toggleCheckbox('{material}')">
            </div>
        """
        
        # Render the div
        st.markdown(div_style, unsafe_allow_html=True)


    # JavaScript function to toggle checkbox
    st.markdown(
        """
        <script>
        function toggleCheckbox(material) {
            fetch("/?material=" + material).then(response => window.location.reload());
        }
        </script>
        """, unsafe_allow_html=True
    )

    if st.button('Continue'):
        st.switch_page("pages/5_Vehicles.py")

    # # Include the CSS in your Streamlit app
    # st.markdown(button_style, unsafe_allow_html=True)

    # # Create a button using HTML
    # st.markdown('<a href="/vehicles" target="_self" class="button">Continue</a>', unsafe_allow_html=True)

        
# material_page()

if __name__ == "__main__":
    
    main()