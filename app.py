#frontend

import streamlit as st
from moondream_lib import mdHelper
from PIL import Image
import requests
from streamlit_lottie import st_lottie

#some initial page config

st.set_page_config(
    page_title="Moondream Dashboard",
    page_icon="🌑"
)

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        st.error("Could not load Lottie animation")
        return None

# Load Lottie animation
lottie_animation = load_lottieurl("https://lottie.host/1cb0007e-584e-4ace-be20-217efa3783ed/ct2geydstY.json")

# Display Lottie animation
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="main_animation")
    
lot2 = load_lottieurl("https://lottie.host/db4b178c-6569-4d21-a04c-4bb94fc99b6a/P7qWRnm1EG.json")


st.title("🌑 Moondream Dashboard")

# Initialize session state for page tracking first, before using it
if 'page' not in st.session_state:
    st.session_state.page = "Describe Image"

# Define callback functions for the buttons to avoid state conflicts
def set_page_describe():
    st.session_state.page = "Describe Image"
    
def set_page_caption():
    st.session_state.page = "Caption Image"
    
# First, add a new callback function for the Author tab
def set_page_author():
    st.session_state.page = "Author"

# Modify your navigation buttons to include an Author tab
st.write("---")
col1, col2, col3 = st.columns(3)  # Change to 3 columns
with col1:
    st.button("📷 Describe Image", on_click=set_page_describe, use_container_width=True)
with col2:
    st.button("🖼️ Caption Image", on_click=set_page_caption, use_container_width=True)
with col3:
    st.button("👤 Author", on_click=set_page_author, use_container_width=True)
st.write("---")

@st.cache_resource
def get_moondream():
    return mdHelper(api_key=st.secrets["moondream_api_key"])

moondream = get_moondream()

def upload_image():
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"], key= f"page_{st.session_state.page}")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="The image you uploaded!")
        return image
    return None

with st.sidebar:
    if lot2:
        st_lottie(lot2, height=200, key="side_anim")
    st.title("Moondream Vision API")
    # Set the index based on current page
    current_index = 0
    if st.session_state.page == "Describe Image":
        current_index = 0
    elif st.session_state.page == "Caption Image":
        current_index = 1
    else:
        current_index = 2
        
    s_page = st.sidebar.radio("Select the page you want to visit", 
                            ["Describe Image", "Caption Image", "Author"],
                            index=current_index)
    st.session_state.page = s_page

    
if st.session_state.page == "Describe Image":
    st.title("📷Describe Image")
    st.write("Upload an image to get the description")
    image = upload_image()
    if image:
        detail = st.radio("Select the description detail", ["Short", "Normal","Long" ], horizontal=True)
        if st.button("Generate  Description"):
            with st.spinner("Analysing Image"):
                description = moondream.describe(image,detail.lower())
                st.success("Description Generated")
                st.write(description)
                
elif st.session_state.page == "Caption Image":
    st.title("✍️Caption Image")
    st.write("Upload an image to get the Caption")
    image = upload_image()
    if image:
        Question = st.text_input("Enter What you want to ask about the image:", placeholder="What is in the image?")
        if st.button("Answer the quesry"):
            with st.spinner("Analysing Image"):
                description = moondream.query(image,Question)
                st.success("Answer Generated")
                st.write(description)
elif st.session_state.page == "Author":
    st.title("👤 About the Author")
    
    # Create a layout with two columns
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Optional: Add a profile picture 
        # You can replace this with st.image() and a local profile picture
        st.image(image="1720381456833.jpg")
    
    with col2:
        st.subheader("Developer Information")
        st.write("""
        **Name:** Akhand Singh  
        **Role:** Junior Year CSE Undergrad | IIT Patna
        
        **About Me:**  
        I'm passionate about computer vision and AI applications. This app demonstrates 
        the capabilities of the Moondream vision model in understanding and describing images.
        
        **Connect with me:**
        """)
        
        # Social media links
        cols = st.columns(3)
        with cols[0]:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)")
        with cols[1]:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)")
        with cols[2]:
            st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourusername)")
    
    # Project information section
    st.subheader("About This Project")
    st.write("""
    This application was built using:
    - Streamlit for the web interface
    - Moondream Vision API for image analysis
    - The project demonstrates computer vision capabilities including image description and visual question answering.
    
    For more information about the Moondream model, visit [their documentation](https://github.com/vikhyat/moondream).
    """)