import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aravind Reddy Gaddam | AI Developer", page_icon="💼", layout="wide")

# --- HERO SECTION ---
st.title("👋 Hi, I'm Aravind Reddy Gaddam")
st.subheader("AI Developer | Data Science Enthusiast | Machine Learning Practitioner")

# --- GITHUB REPO BUTTON ---
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)](https://github.com/A-cyber-cmyk/portfolio_ap)")

# --- ABOUT ---
st.markdown("---")
st.header("About Me")
st.write("""
I'm an aspiring AI Developer with a strong passion for Machine Learning and Data Science.
I have completed internships in Data Visualization, AI, and Virtual Internships with Deloitte & Microsoft.
I enjoy building projects that solve real-world problems.
""")

# --- CERTIFICATIONS ---
st.markdown("---")
st.header("🎓 Certifications & Achievements")
certifications = [
    "🏅 Data Visualization by TATA",
    "🏅 AI for Beginners by HP",
    "🏅 Virtual Internship by Deloitte",
    "🏅 Machine Learning – Microsoft",
    "🏅 Introduction to AI – Microsoft"
]
for cert in certifications:
    st.write(cert)

# --- DOWNLOAD RESUME BUTTON ---
with open("aravind_resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name="Aravind_Reddy_Gaddam_Resume.pdf",
        mime="application/pdf"
    )

# --- SPACING ---
st.markdown("<br><br>", unsafe_allow_html=True)

# --- CONTACT INFO ---
st.markdown("---")
st.header("Let's Connect 🤝")
st.write("📧 **Email**: aravindreddyking0@gmail.com")
st.write("[🔗 LinkedIn Profile](https://www.linkedin.com/in/aravind-reddy-gaddam-63a052278/)")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2025 Aravind Reddy Gaddam | All Rights Reserved")
