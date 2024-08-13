import base64

# background_image_path = '/Users/hishammohammed/Desktop/personal_project/scrapdaddy/hackathon/images/bg_20.jpg'
background_image_path = './images/bg_27.jpg'
sustainable_logo_path = './images/sustainable.png'
recyclable_logo_path = './images/recyclable.png'
zero_waste_logo_path = './images/zero_waste.png'
home_page_icon = './images/home_page_icon.png'
signup_logo_path = './images/signup.png'
materials_logo_path = './images/materials.png'
pickup_logo_path = './images/pickup.png'
money_logo_path = './images/money.png'

# home_font_path = './fonts/PlayfairDisplay-VariableFont_wght.ttf'
# home_font_path = './fonts/Platypi-VariableFont_wght.ttf'
home_font_path = './fonts/BodoniModa-VariableFont_opsz,wght.ttf'




category_logos = {
    'Individual': './logos/avatar.png',
    'Enterprises': './logos/enterprise.png'
}
vehicles = ['3 Wheeler', 'Tata Ace', '14 ft Truck', 'Tata 407']
limits = {
    '3 Wheeler': 50,
    'Tata Ace': 100,
    '14 ft Truck': 150,
    'Tata 407': 200
}
vehicle_logos = {
    '3 Wheeler': './logos/three-wheeler.png',
    'Tata Ace': './logos/delivery.png',
    '14 ft Truck': './logos/14ft_2.png',
    'Tata 407': './logos/truck.png'
}

logo = './images/recycling_5.png'
link_url = ""
def clickable_image(image_path, link_url, width, height):
    with open(image_path, "rb") as image_file:
        image = image_file.read()
    img_str = base64.b64encode(image).decode()

    html_code = f"""
    <a href="{link_url}" target="_self">
        <img src="data:image/jpeg;base64,{img_str}" style="width:{width}px; height:{height}px; max-width:100%;">
    </a>
    """
    return html_code

# image_css = """
# <style>
# [data-testid="stSidebarUserContent"] {
#     padding: 0.001rem !important;
#     margin: 0 !important;
# }
# div[data-testid="stButton"] {
#     display: flex;
#     justify-content: center; /* Center-aligns the button horizontally */
#     align-items: center; /* Center-aligns the button vertically */
#     padding-left: 1rem; /* Adds padding to the left */
# }
# </style>
# """
image_css = ""