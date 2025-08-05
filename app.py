
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aravind Reddy Gaddam | AI Developer Portfolio", page_icon="💼", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
        .hero {
            text-align: center;
            padding: 2rem 1rem;
            background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
            color: white;
            border-radius: 12px;
            margin-bottom: 2rem;
        }
        .hero h1 {
            font-size: 3rem;
        }
        .hero a {
            background-color: #0A66C2;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            font-size: 1.1rem;
        }
        .section-title {
            font-size: 2rem;
            font-weight: bold;
            background: -webkit-linear-gradient(#0A66C2, #005983);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid rgba(255,255,255,0.2);
        }
        .download-btn {
            background-color: #0A66C2;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="hero">
        <h1>Aravind Reddy Gaddam</h1>
        <p>AI Developer | Python Enthusiast | Machine Learning Practitioner</p>
        <a href="https://www.linkedin.com/in/aravind-reddy-gaddam-63a052278/" target="_blank">Visit LinkedIn</a>
    </div>
""", unsafe_allow_html=True)

# --- ABOUT ME ---
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.write("""
Motivated AI Developer currently pursuing B.Tech in Computer Science (AI & ML) at Mohan Babu University.
Proficient in Python, Machine Learning, and AI frameworks. Experienced in AI-powered applications,
including Retrieval-Augmented Generation (RAG) systems and intelligent gaming agents.
Passionate about delivering innovative AI solutions with analytical thinking and problem-solving.
""")

# --- SKILLS ---
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><strong>Technical Skills</strong><ul><li>Python Programming</li><li>Data Structures & Algorithms</li><li>Machine Learning</li><li>AI Tools & Frameworks</li></ul></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><strong>Soft Skills</strong><ul><li>Problem Solving</li><li>Analytical Thinking</li><li>Team Collaboration</li><li>Adaptability & Learning Agility</li></ul></div>', unsafe_allow_html=True)

# --- PROJECTS ---
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><strong>AI Playing Agent</strong><p>Developed AI-powered games enhancing user engagement and cognitive skills across multiple platforms.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><strong>Retrieval-Augmented Generation (RAG) System</strong><p>Built a document-based intelligent Q&A system using advanced NLP models for coherent responses.</p></div>', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><strong>B.Tech in CSE (AI & ML)</strong> | Mohan Babu University | Expected 2026 | CGPA: 8.37</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><strong>Intermediate (10+2)</strong> | Narayana Junior College | 2022 | 86%</div>', unsafe_allow_html=True)
st.markdown('<div class="card"><strong>High School</strong> | Chaitanya Bharathi High School | 2020 | 96.16%</div>', unsafe_allow_html=True)

# --- CERTIFICATIONS ---
st.markdown('<div class="section-title">Certifications & Achievements</div>', unsafe_allow_html=True)
cert_list = [
    "Data Visualization by TATA",
    "AI for Beginners by HP",
    "Virtual Internship by Deloitte",
    "Machine Learning – Microsoft",
    "Introduction to AI – Microsoft"
]
for cert in cert_list:
    st.markdown(f'<div class="card">🏅 {cert}</div>', unsafe_allow_html=True)

# --- DOWNLOAD RESUME BUTTON ---
with open("aravind_resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    st.download_button(label="📄 Download My Resume", data=PDFbyte, file_name="Aravind_Reddy_Gaddam_Resume.pdf", mime='application/pdf')

# --- CONTACT ---
st.markdown("---")
st.header("Let's Connect")
st.write("📧 Email: aravindreddyking0@gmail.com")
st.write("[LinkedIn Profile](https://www.linkedin.com/in/aravind-reddy-gaddam-63a052278/)")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2025 Aravind Reddy Gaddam | All Rights Reserved")
