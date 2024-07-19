def load_sidebar_styles():
    return """
        <style>

        div[data-testid="stSidebarNav"] li div a {
            margin-left: 1rem;
            padding: 0.5rem;
            width: 200px;
            font-color: #ffffff;
            border-radius: 0.25rem;
            background-color: rgba(201, 233, 250, 1);
            /* border: 1px solid lightgrey; */
        }
        [data-testid="stSidebarContent"] {
            background-color: #f7f8fa;
            padding: 20px;
            border-radius: 10px;
            font-size: 16px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "SCRAPDADDY";
            font-size: 30px;
            position: relative;
            margin-left: 1rem;
            font-family: 'Chalkduster', fantasy; /* Add your desired font family here */
            font-weight: bold; /* Make the text bold */
            display: block;
            padding-bottom: 20px;
        }  
        [data-testid="stSidebarHeader"] {
        /* Add your desired styles here */
        padding: 2px;
        height: 20px;
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
            font-size: 10px; /* Adjust font size */
            font-family: Arial, sans-serif;
            color: white !important;
            margin-left: 20px; /* Add margin to the left */
            text-decoration: none;
            width: 200px; /* Adjust width */
            height: 40px; /* Adjust height */
        }
        .category-button img {
            width: 25px;
            height: auto;
            margin-left: 10px;
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