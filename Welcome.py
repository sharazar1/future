import streamlit as st
import streamlit.components.v1 as components
import base64

# Set Streamlit page configuration
st.set_page_config(
    page_title="welcome Visitor!",
    page_icon="✨",
    layout="wide"
)

# Path to your profile picture
image_path = "./static/profile-picture.jpg"

# Function to encode the image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        return base64.b64encode(img_bytes).decode()

# Convert image to base64
image_base64 = image_to_base64(image_path)

# HTML Code with Profile Picture and Title
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Particles Background</title>
    <style>
        /* Full height for the body and particles container */
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }}

        #particles-js {{
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1; /* Background layer */
            background-color: #000; /* Black background */
        }}

        /* Centered content */
        .content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            font-family: Arial, sans-serif;
        }}

        .content img {{
            width: 150px; /* Adjust size of the profile picture */
            height: 150px; /* Ensure it's a square */
            border-radius: 50%; /* Make it round */
            border: 3px solid white; /* Add a white border for aesthetics */
            margin-bottom: 20px; /* Space between image and title */
        }}

        .content h1 {{
            font-size: 3em;
            margin: 0;
        }}

        .content p {{
            font-size: 1.2em;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <!-- Particles.js container -->
    <div id="particles-js"></div>

    <!-- Centered content -->
    <div class="content">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Profile Picture">
        <h1>Sharazar Munawar</h1>
        <h2>Bridging the Gap between Data, Decisions and Infrastructure</h2>
        <p>Data Analytics | Visualization | Infrastructure Modernization | Project Leadership</p>
    </div>

    <!-- Particles.js script -->
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {{
            "particles": {{
                "number": {{
                    "value": 80,
                    "density": {{
                        "enable": true,
                        "value_area": 800
                    }}
                }},
                "color": {{
                    "value": "#ffffff"
                }},
                "shape": {{
                    "type": "circle",
                    "stroke": {{
                        "width": 0,
                        "color": "#000000"
                    }}
                }},
                "opacity": {{
                    "value": 0.5,
                    "random": false
                }},
                "size": {{
                    "value": 3,
                    "random": true
                }},
                "line_linked": {{
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                }},
                "move": {{
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }}
            }},
            "interactivity": {{
                "detect_on": "canvas",
                "events": {{
                    "onhover": {{
                        "enable": true,
                        "mode": "repulse"
                    }},
                    "onclick": {{
                        "enable": true,
                        "mode": "push"
                    }}
                }},
                "modes": {{
                    "repulse": {{
                        "distance": 100,
                        "duration": 0.4
                    }},
                    "push": {{
                        "particles_nb": 4
                    }}
                }}
            }},
            "retina_detect": true
        }});
    </script>
</body>
</html>
"""

# Embed the HTML into Streamlit
components.html(html_code, height=600, scrolling=False)


# sidebar next

with st.sidebar:

    # LinkedIn button with GIF
    linkedin_gif_path = "./static/linkedin.gif"  # Path to your LinkedIn GIF
    with open(linkedin_gif_path, "rb") as f:
        linkedin_gif = f.read()
    
    # Use st.sidebar.markdown to embed the GIF as a clickable link
    st.sidebar.markdown(
        f"""
        <a href="https://www.linkedin.com/in/sharazar/" target="_blank">
            <img src="data:image/gif;base64,{base64.b64encode(linkedin_gif).decode()}" alt="LinkedIn" style="width: 30px; height: 35px;">
        </a>
        """,
        unsafe_allow_html=True,
    )