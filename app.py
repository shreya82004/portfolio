import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Shreya Amar Kasture | Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("Shreya Amar Kasture")
st.subheader("Final Year CSE (Honors in Data Science) Student")

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
st.markdown("© 2025 Shreya Amar Kasture | Built with Python & Streamlit")
