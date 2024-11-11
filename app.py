import streamlit as st 
import requests
import base64
from PIL import Image 
import io

st.title("IMG AI-Artist")
st.write("Turning Words into Art with AI")


# Add siderbar for configuration 
st.sidebar.header("Configuration")
api_url = st.sidebar.text_input(
    "Backend API URL",
    "https://da6b-34-168-158-3.ngrok-free.app" # you will replace this with the ngrok url from colab
)


# main interface 
text_prompt = st.text_input("Enter your prompt","A beautiful sunset over mountains")
if st.button("Generate Image"):
    if not api_url:
        st.error("please enter the backend API URL in the sidebar")
        
        
    with st.spinner("Generating image..."):
        try:
            response = requests.post(
                f"{api_url}/generated",
                json = {"text":text_prompt}
            )

            if response.status_code == 200:
                # Decode and display the image 
                image_data = base64.b64decode(response.json()["image"])
                image  = Image.open(io.BytesIO(image_data))
                st.image(image,caption="Generated Image")
            else:
                st.error (f"Failed to generate image. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error:{str(e)}")
            
            
st.markdown("""
### Tips for better prompts:
- Be specific in your descriptions 
- Include details about style, lighting, and composition 
- Try different variations of your prompt                     
""")