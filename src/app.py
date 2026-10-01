import streamlit as st
from pathlib import Path
import sys


# --------------------------------------------------
# Find the project folder
# --------------------------------------------------

project_folder = Path(__file__).resolve().parent.parent

# Allow Python to find chatbot.py
sys.path.append(str(Path(__file__).resolve().parent))

from chatbot import FAQChatbot


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main application background */
    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(37, 99, 235, 0.25),
                transparent 35%
            ),
            radial-gradient(
                circle at bottom right,
                rgba(124, 58, 237, 0.20),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #0f172a,
                #111827,
                #020617
            );

        color: white;
    }


    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 5px;
        color: white;
    }


    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }


    /* Information box */
    .info-box {
        background: rgba(255, 255, 255, 0.07);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin-bottom: 25px;
        color: #e2e8f0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
    }


    /* User message */
    .user-message {
        background: linear-gradient(
            135deg,
            #2563eb,
            #3b82f6
        );

        color: white;
        padding: 13px 17px;
        border-radius: 16px;
        margin: 12px 0;

        box-shadow:
            0 5px 15px rgba(37, 99, 235, 0.25);
    }


    /* Bot message */
    .bot-message {
        background: rgba(255, 255, 255, 0.07);
        color: #f1f5f9;
        padding: 16px 18px;
        border-radius: 16px;
        margin: 10px 0 20px 0;

        border: 1px solid rgba(255, 255, 255, 0.10);

        box-shadow:
            0 5px 20px rgba(0, 0, 0, 0.20);
    }


    /* Chat input */
    [data-testid="stChatInput"] {
        background-color: white !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 12px !important;
    }


    /* Text typed by the user */
    [data-testid="stChatInput"] textarea {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        background-color: white !important;
        caret-color: #000000 !important;
    }


    /* Placeholder text */
    [data-testid="stChatInput"] textarea::placeholder {
        color: #64748b !important;
        -webkit-text-fill-color: #64748b !important;
        opacity: 1 !important;
    }


</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Load FAQ chatbot
# --------------------------------------------------

faq_file = project_folder / "data" / "faqs.json"

chatbot = FAQChatbot(faq_file)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI FAQ Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about Artificial Intelligence, NLP, '
    'Computer Vision, Object Detection and AI Music Generation.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Information Box
# --------------------------------------------------

st.markdown(
    """
    <div class="info-box">

    <b>💡 Try asking:</b>

    <br><br>

    • What is YOLO?<br>
    • What is object detection?<br>
    • How can AI create music?<br>
    • What is TF-IDF?<br>
    • What is NLP?<br>
    • What is machine learning?

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Create chat history
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                <b>You:</b> {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-message">
                <b>🤖 AI Assistant:</b><br><br>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# User input
# --------------------------------------------------

user_question = st.chat_input(
    "Ask me anything about AI..."
)


# --------------------------------------------------
# Process user question
# --------------------------------------------------

if user_question:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # Get chatbot response
    answer, score = chatbot.get_response(
        user_question
    )


    # Add chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    # Refresh the application
    st.rerun()