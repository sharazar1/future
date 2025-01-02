import streamlit as st
import base64

def get_video_as_base64(video_path):
    # Convert the video file into a base64 string
    with open(video_path, "rb") as video_file:
        video_base64 = base64.b64encode(video_file.read()).decode("utf-8")
    return video_base64

# Path to your video and image
video_path = "static/BG.mp4"
image_path = "static/profile-picture.jpg"

# Encode the video to base64
video_base64 = get_video_as_base64(video_path)

# Streamlit HTML and CSS with inline styling
st.markdown(
    f"""
    <style>
        /* Full-page container with video background */
        .video-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }}

        /* Video as the background */
        .video-container video {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            min-width: 100%;
            min-height: 100%;
        }}

        /* Content container for profile picture and text */
        .content {{
            position: relative;
            text-align: center;
            color: white;
            font-family: Arial, sans-serif;
            top: 50%;
            transform: translateY(-50%);
        }}

        /* Circular profile picture */
        .content img {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 3px solid white;
            margin-bottom: 20px;
        }}

        /* Heading and subheading styles */
        .content h1 {{
            font-size: 2.5rem;
            margin: 0;
        }}

        .content p {{
            font-size: 1.2rem;
            margin: 10px 0;
        }}
    </style>
    <div class="video-container">
        <!-- Base64 encoded video -->
        <video autoplay muted loop>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

    <div class="content">
        <!-- Profile picture and text overlay -->
        <img src="{image_path}" alt="Profile Picture">
        <h1>Your Name</h1>
        <p>Data Analyst | Visualization Expert | Infrastructure Modernization Specialist</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Optional: Add interactive Streamlit components below
st.write("You can add more interactive components here!")
