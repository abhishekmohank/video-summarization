import streamlit as st
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
import os
import tempfile
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Load API key from secrets
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    client = Groq(api_key=groq_api_key)
else:
    st.error("GROQ API key not found. Please check your configuration.")

# Set Page Configuration
st.set_page_config(page_title="CineMind: AI-Driven Contextual Video Summarization", page_icon="🎥", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .title {text-align: center; font-size: 50px; font-weight: bold; color: #FF4B4B;}
        .subtitle {text-align: center; font-size: 22px; font-weight: 500; color: #6C757D;}
        .analyze-btn {background-color: #FF4B4B; color: white; font-size: 18px; padding: 10px 20px; border-radius: 10px;}
        .result-container {background-color: #f8f9fa; padding: 20px; border-radius: 10px; color: black;}
    </style>
    """,
    unsafe_allow_html=True
)

# Display Title & Subtitle
st.markdown('<h1 class="title">CineMind: AI-Driven Contextual Video Summarization 🎬</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Transform lengthy videos into concise summaries using AI.</p>', unsafe_allow_html=True)

# Author Section
st.markdown("### 🔥 Built with passion by **Muhammad Shoaib** 🚀")

# Cache DuckDuckGo Initialization
@st.cache_resource()
def initialize_duckduckgo():
    return DuckDuckGo()

# Initialize tools
search_tool = initialize_duckduckgo()

# File Uploader with Expander for Clean UI
with st.expander("📤 Upload Video File (mp4, mov, avi)"):
    video_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"], help="Upload a video for AI analysis.")

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name
    
    st.video(video_path, format="video/mp4", start_time=0)
    
    user_query = st.text_area("🔍 What insights are you seeking?", placeholder="Ask anything about the video content...")
    
    if st.button("Analyze Video", key="analyze_video_button", help="Click to process the video"):
        if not user_query:
            st.warning("Please enter a question to analyze the video.")
        else:
            try:
                with st.spinner("🚀 Processing video and gathering insights..."):
                    
                    # Simulated progress bar
                    progress_bar = st.progress(0)
                    for i in range(100):  
                        time.sleep(0.02)  
                        progress_bar.progress(i + 1)
                    
                    # Generating response using Groq API
                    analysis_prompt = f"""
                    Analyze the following video content and answer the user's query:
                    {user_query}
                    Supplement the response with relevant insights.
                    """
                    
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": analysis_prompt}],
                        model="deepseek-r1-distill-llama-70b",
                    )
                    
                    response = chat_completion.choices[0].message.content
                    
                    # Display result in an interactive container
                    st.markdown("### 📊 Analysis Result")
                    st.markdown(f'<div class="result-container">{response}</div>', unsafe_allow_html=True)
            
            except Exception as error:
                st.error(f"⚠️ An error occurred: {error}")
            
            finally:
                if os.path.exists(video_path):
                    os.unlink(video_path)
