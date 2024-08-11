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
    