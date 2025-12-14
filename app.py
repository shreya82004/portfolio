import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Shreya Amar Kasture | Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- GLOBAL COLOR THEME ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

a {
    color: #4cc9f0 !important;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

hr {
    border: 1px solid #444;
}

strong {
    color: #ffd166;
}

.footer {
    color: #cccccc;
    text-align: center;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PROFILE SECTION ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.png", width=180)

with col2:
    st.markdown(
        """
        <p style="font-size:26px; font-weight:600; margin-bottom:5px;">
            Hi There 👋,
        </p>
        <p style="font-size:38px; font-weight:800; margin-top:0;">
            I'm <span style="color:#ff7a00;">Shreya Amar Kasture</span>
        </p>
        <p style="font-size:22px; color:#ffd166;">
            Final Year CSE (Honors in Data Science) Student
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------- CONTACT ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("📧 **Email**")
    st.write("shreyakasture7@gmail.com")

with c2:
    st.markdown("🔗 **LinkedIn**")
    st.markdown("[View Profile](https://www.linkedin.com/in/shreya-kasture-409494259)")

with c3:
    st.markdown("🐙 **GitHub**")
    st.markdown("[View GitHub](https://github.com/shreya82004)")

st.markdown("---")

# ---------------- ABOUT ----------------
st.header("About Me")
st.write(
    "I am a final year Computer Science Engineering student (Honors in Data Science) with a strong "
    "interest in Python, data analysis, and machine learning. I enjoy working on data-driven "
    "projects and converting raw data into meaningful insights."
)

# ---------------- EDUCATION ----------------
st.header("Education")
st.write(
    "**B.Tech in Computer Science Engineering**  \n"
    "Walchand Institute of Technology, Solapur  \n"
    "2022 – 2026"
)

# ---------------- EXPERIENCE ----------------
st.header("Experience")
st.write(
    "**Winter Training Intern – Remote Sensing & GIS**  \n"
    "Indian Space Academy (Remote)  \n"
    "January 2026"
)

# ---------------- SKILLS ----------------
st.header("Skills")
st.markdown("""
- **Programming:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn  
- **Databases:** SQL  
- **Machine Learning:** Scikit-learn  
- **Core CS:** Data Structures & Algorithms, OS, CN, DBMS  
""")

# ---------------- PROJECTS ----------------
st.header("Projects")

st.subheader("Heart Disease Analysis")
st.write(
    "Performed exploratory data analysis (EDA) on heart disease datasets to identify "
    "important health risk factors and trends using Python visualization libraries."
)
st.markdown("[🔗 View on GitHub](https://github.com/shreya82004/heart-disease-analysis)")

st.subheader("Vaccination Data Analytics")
st.write(
    "Analyzed vaccination datasets and created meaningful visualizations to understand "
    "vaccination trends and coverage."
)
st.markdown("[🔗 View on GitHub](https://github.com/shreya82004/vaccination-analytics)")

# ---------------- CERTIFICATIONS ----------------
st.header("Certifications")
st.markdown("""
- **Infosys Python Foundation** – Python fundamentals and problem-solving  
- **SQL Basics to Expert (Udemy)** – SQL queries, joins, subqueries, database concepts  
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div class='footer'>© 2025 Shreya Amar Kasture | Built with Python & Streamlit</div>",
    unsafe_allow_html=True
)
