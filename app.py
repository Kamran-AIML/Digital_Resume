import streamlit as st
from PIL import Image
import base64
import requests


# --- PATH SETTINGS ---
PROFILE_PIC = "assets/profile_pic_1.jpg"
RESUME_FILE = "assets/resume.pdf"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Kamran's Digital Resume", page_icon=":briefcase:", layout="wide")

# --- LOAD ASSETS ---
profile_pic = Image.open(PROFILE_PIC)

# --- SIDEBAR ---
# --- SIDEBAR ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("Kamran Shaikh")
    st.markdown("**AI/ML Engineer**")
    st.markdown("📍 Mumbai, India")

    # st.markdown("---")
    st.markdown("<hr style='margin:0;'>", unsafe_allow_html=True)

    st.markdown("### Connect with Me")

    st.markdown("📧 kamran.aiml.engineer@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/kamran-shaikh-10a155240/)")
    # st.markdown("🐙 [GitHub](https://github.com/Kamran-AIML)")

    # GitHub logo button (image with link)
    with open("assets/GitHub_Logo.PNG", "rb") as img_file:
        github_logo = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <a href="https://github.com/Kamran-AIML" target="_blank">
            <img src="data:image/png;base64,{github_logo}" width="24" style="vertical-align:middle;margin-right:10px"/>
            <span style="font-size:16px;">GitHub</span>
        </a>
        """,
        unsafe_allow_html=True
    )

    # st.markdown("---")
    # 🧱 Add this line to fix spacing
    st.write("")
    # Download_Resume_button
    st.download_button("📄 Download Resume", open(RESUME_FILE, "rb").read(), file_name="Kamran_Shaikh_Resume.pdf")

# --- ABOUT ---
st.title("About Me")
st.write("""
NLP-focused AI/ML Engineer passionate about building intelligent, language-driven solutions.
I specialize in Document AI, OCR, and LLM applications — developing tools that convert complex data into usable insights.
My tech stack includes FastAPI, LangChain, OpenAI, and Streamlit, enabling rapid development and deployment of production-ready ML systems.
""")

# --- SKILLS ---
st.header("Skills")
st.subheader("🔧 Core Skills")
st.markdown("""
- **LLMs & Agents:** RAG, LangChain, GPT-4, LLaMA, LangGraph, Tool-using agents  
- **ML & DL:** CNN, LSTM, GANs, PyTorch, TensorFlow, Keras  
- **NLP & Doc AI:** BERT, SpaCy, Azure OCR, YOLO, OpenCV, Tesseract  
- **Automation:** Python, FastAPI, Selenium, Regex  
- **Deployment:** Streamlit, Docker, AWS EC2/S3, Linux  
- **Data Engineering:** Web scraping, pipelines, SQL, ChromaDB
""")

# --- EXPERIENCE ---
st.header("Work Experience")

st.subheader("Machine Learning Engineer – HealthIndia Insurance TPA (Apr 2024 – Present)")
st.write("""
- Automated healthcare document processing using LLMs and Azure OCR  
- Built pipelines for NEFT extraction, CCN generation & invoice parsing  
- Deployed scalable FastAPI-based tools in production environments
""")

st.subheader("Python Developer – DG Market (Apr 2023 – Apr 2024)")
st.write("""
- Created APIs and automation tools for tender analytics  
- Scraped, transformed, and stored large volumes of structured/unstructured data
""")

st.subheader("Associate Engineer – Ardentisys-Tebillion (Oct 2022 – Mar 2023)")
st.write("""
- Built backend modules and APIs for business automation tools  
- Contributed to scalable enterprise product logic using Python
""")

# --- PROJECTS ---
st.header("Projects")

st.markdown("🔹 **Document Classification System** – YOLO, CNN, LSTM")
st.markdown("Automated pipeline combining object detection + image/text classification.")

st.markdown("🔹 **Auto NEFT Extraction** – YOLOv8s, Tesseract")
st.markdown("Extracted cheque data using OCR and regex post-processing.")

st.markdown("🔹 **Auto CCN Generation** – Azure OCR, LLaMA")
st.markdown("Generated CCNs from healthcare forms using LLM + OCR pipeline.")

st.markdown("🔹 **PDF Chatbot** – LangChain, ChromaDB")
st.markdown("Built a chatbot to answer questions from uploaded PDFs.")

st.markdown("🔹 **BTC Price Predictor** – LSTM, Python")
st.markdown("[GitHub Link](https://github.com/Kamran-AIML/BTC_Price_Prediction) – Time-series model to forecast Bitcoin prices.")

st.markdown("🔹 **Face Recognition Attendance System** – OpenCV, Dlib")
st.markdown("Live facial recognition for employee attendance logging.")

# --- EDUCATION ---
st.header("Education")
st.write("**B.E in Electronics Engineering** – M.H. Saboo Siddik College of Engineering (2015–2021)")
st.write("**Diploma in Electronics Engineering** – Thakur Polytechnic (2012–2015)")

# --- CONTACT ---
st.header("Get in Touch")
st.markdown("""
📧 kamran.aiml.engineer@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kamran-shaikh-10a155240/)
""")
