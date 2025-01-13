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
            background-color: #272b2e;
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
        <h2>Bridging the Gap between Teams, Data, Decisions and Infrastructure</h2>
        <h3>Driving success through innovation, efficiency, and collaboration.</h3>
        <p>Specializing in Data Analytics | Visualization | Infrastructure Modernization | Project Leadership | Team Management</p>
    </div>

    <!-- Particles.js script -->
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {{
            "particles": {{
                "number": {{
                    "value": 300,
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
                "polygon": {{
                "nb_sides": 5
                }},
                "opacity": {{
                    "value": 0.5,
                    "random": false,
                }},
                "size": {{
                    "value": 3,
                    "random": false,
                    "anim": {{
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.2,
                    "sync": false
                    }}
                }},
                "size": {{
                "value": 2,
                "random": true,
                "anim": {{
                "enable": false,
                "speed": 40,
                "size_min": 0.1,
                "sync": false
                }}
                }},
                "line_linked": {{
                    "enable": true,
                    "distance": 100,
                    "color": "#ffffff",
                    "opacity": 0.22,
                    "width": 1
                }},
                "move": {{
                    "enable": true,
                    "speed": 0.2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": true,
                    "attract": {{
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                    }}
                }}
            }},
            "interactivity": {{
                "detect_on": "canvas",
                "events": {{
                    "onhover": {{
                        "enable": true,
                        "mode": "grab"
                    }},
                    "onclick": {{
                        "enable": true,
                        "mode": "push"
                    }},
                    "resize": true
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
e
with st.sidebar:

    # LinkedIn button with GIF
    linkedin_gif_path = "./static/linkedin.gif"  # Path to your LinkedIn GIF
    with open(linkedin_gif_path, "rb") as f:
        linkedin_gif = f.read()

    # Email button with GIF
    email_gif_path = "./static/email.gif"  # Path to email GIF
    with open(email_gif_path, "rb") as f:
        email_gif = f.read()

    # whatsapp button with GIF
    whatsapp_gif_path = "./static/whatsapp.gif"  # Path to whatsapp GIF
    with open(whatsapp_gif_path, "rb") as f:
        whatsapp_gif = f.read()

    # call button with GIF
    call_gif_path = "./static/call.gif"  # Path to call GIF
    with open(call_gif_path, "rb") as f:
        call_gif = f.read()

    # Use st.sidebar.markdown to embed the GIF as a clickable link
    st.sidebar.markdown(
        f"""
        <div style="display: flex; flex-direction: row; gap: 50px;">
            <!-- LinkedIn Button -->
            <a href="https://www.linkedin.com/in/sharazar/" target="_blank">
                <img src="data:image/gif;base64,{base64.b64encode(linkedin_gif).decode()}" alt="LinkedIn" style="width: 30px; height: 30px;">
            </a>
            <!-- Email Button -->
            <a href="mailto:sharazar00@gmail.com">
            <img src="data:image/gif;base64,{base64.b64encode(email_gif).decode()}" alt="Email" style="width: 25px; height: 25px;">
            </a>
            <!-- Whatsapp Button -->
            <a href="https://wa.me/923055604285?text=Hello!%20I%27d%20love%20to%20hear%20more%20about%20how%20we%20can%20work%20together.%20Feel%20free%20to%20share%20your%20ideas%20or%20questions%E2%80%94I%27m%20looking%20forward%20to%20chatting%20with%20you!">
            <img src="data:image/gif;base64,{base64.b64encode(whatsapp_gif).decode()}" alt="Email" style="width: 25px; height: 25px;">
            </a>
            <!-- call Button -->
            <a href="tel:+923055604285">
            <img src="data:image/gif;base64,{base64.b64encode(call_gif).decode()}" alt="Call" style="width: 25px; height: 25px;">
            </a>
            

        </div>
        """,
        unsafe_allow_html=True,
    )


# timeline Below


# Embed the updated timeline HTML/CSS
components.html(
    """
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: rgba(207, 203, 212, 0.2);
            color: #333;
        }

        .timeline {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #00BFAE;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }

        .timeline li {
            padding: 10px 0;
            position: relative;
            list-style: none;
        }

        .timeline li::before {
            content: '';
            position: absolute;
            width: 15px;
            height: 15px;
            background-color: #00BFAE;
            border-radius: 50%;
            left: 50%;
            margin-left: -7.5px;
            top: 0;
        }

        .timeline .container {
            padding: 20px;
            background-color: white;
            position: relative;
            border-radius: 6px;
            width: 45%;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }

        .timeline .container.left {
            left: 0;
        }

        .timeline .container.right {
            left: 50%;
        }

        .timeline .content {
            padding: 20px;
            background-color: #00BFAE;
            color: white;
            border-radius: 6px;
        }

        .timeline .content h3 {
            margin: 0 0 10px;
            font-size: 18px;
        }

        .timeline .content p {
            margin: 0;
            font-size: 14px;
        }

        .timeline .year {
            font-size: 18px;
            font-weight: bold;
        }
    </style>

    <div class="timeline">
        <ul>
            <!-- Section: My Experiences -->
            <li>
                <div class="container left">
                    <div class="content">
                        <h3 style="font-family: Comic Sans MS;">My Experiences</h3>
                        <p><b>2020:</b> Started my journey into data analytics during my BBA in Finance. Worked on finance-related case studies and projects where I learned management principles and data driven decision making.</p>
                    </div>
                </div>
            </li>
            <li>
                <div class="container right">
                    <div class="content">
                        <h3 style="font-family: Comic Sans MS;">My Experiences</h3>
                        <p><b>2022: </b>Gained practical experience applying data-driven decision-making to HR, management, and finance in organizational settings. Managed remote teams</p>
                    </div>
                </div>
            </li>

            <!-- Section: My Certifications -->
            <li>
                <div class="container left">
                    <div class="content">
                        <h3 style="font-family: Comic Sans MS;">My Certifications</h3>
                        <p><b>2020 to 2023:</b> Completed certifications in Python, SQL, and Power BI, equipping myself with essential tools for data analytics. Learned essential team managment strategies, disaster response strategies and crisi managment from Google.</p>
                    </div>
                </div>
            </li>

            <!-- Section: My Expertise -->
            <li>
                <div class="container right">
                    <div class="content">
                        <h3 style="font-family: Comic Sans MS;">My Expertise</h3>
                        <p style="margin-bottom: 10px;">Proficient in integrating data anlytics and financal data to make strategic, data-driven decisions that impact organizational growth.</p>
                        <p>I Understand the importance of organizational cultue in maintaining organizational success.</p>
                    </div>
                </div>
            </li>

            <!-- Section: How it all comes together -->
            <li>
                <div class="container left">
                    <div class="content">
                        <h3 style="font-family: Comic Sans MS;">How It All Comes Together</h3>
                        <p style="margin-bottom: 10px;">My unique combination of skills allows me to bridge the gap between analytics and strategic decision-making in diverse organizational fields.</p>
                        <p>I work to build an organizational culture which supports organizational sucess, driving all decision making from decisions grounded in real world data.</p>
                    </div>
                </div>
            </li>
        </ul>
    </div>
    """,
    height = 1600,  # Adjust height as needed
)