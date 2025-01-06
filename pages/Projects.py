import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page configuration
st.set_page_config(
    page_title="Particles Background",
    page_icon="✨",
    layout="wide"
)

# Define HTML for the particles background
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Particles Background</title>
    <style>
        /* Full height for the body and particles container */
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }

        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1; /* Background layer */
            background-color: #000; /* Black background */
        }

        /* Centered content */
        .content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            font-family: Arial, sans-serif;
        }

        .content h1 {
            font-size: 3em;
            margin: 0;
        }

        .content p {
            font-size: 1.2em;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <!-- Particles.js container -->
    <div id="particles-js"></div>

    <!-- Centered content -->
    <div class="content">
        <h1>Welcome to My Website</h1>
        <p>Data Analytics | Visualization | Infrastructure Modernization</p>
    </div>

    <!-- Particles.js script -->
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {
                    "value": 80,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.5,
                    "random": false
                },
                "size": {
                    "value": 3,
                    "random": true
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "repulse"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    }
                },
                "modes": {
                    "repulse": {
                        "distance": 100,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    }
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

# Embed the HTML into Streamlit
components.html(html_code, height=600, scrolling=False)
