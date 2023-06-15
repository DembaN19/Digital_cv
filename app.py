from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Demba Ndiaye"
PAGE_ICON = ":wave:"
NAME = "Demba Ndiaye"
DESCRIPTION = """
Data Analyst Junior, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "jacksonjaay1919@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/demba-n-965146146/",
    "GitHub": "https://github.com/DembaN19"
}
PROJECTS = {
    "🏆 Streamlit App with multiple dashboards for Analysis - Inventory Management",
    "🏆 VBA project - Making a report for suppliers returns for Accounting processing",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong hands on experience with accounting and P&L
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Streamlit
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Veepee**")
st.write("03/2023 - Present")
st.write(
    """
- ► Developed a Stream lit app with multiple dashboards to track and analyze issues and necessary fixes using Python and Streamlit
- ► Built a data model for predicting use cases and conducted corrective actions, resulting in a 12% improvement in predictions.
- ► Redesigned data model through iterations that improved predictions by 12%
- ► Utilized Python and SQL to redefine and monitor marketing KPIs, leading to a 38% boost in landing page conversion rate and providing recommendations.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Accountant | Veepee**")
st.write("10/2021 - 02/2023")
st.write(
    """
- ► Monitored and analyzed unmatched purchase orders.
- ► Matched purchase orders with supplier invoices and entered invoices in SAP S/4HANA.
- ► Created a macro in Excel VBA to enhance the tracking of shipments and goods receipts for Dropshipment, Cross-Dock, and Pre-Reception processes
- ► Designed a dashboard using Power BI to analyze and facilitate the interpretation of financial data
- ► Automated processes using App Script, enabling automatic updates to the accounting tracking table
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Account Payable | Helexia Developpement**")
st.write("03/2021 - 09/2021")
st.write(
    """
- ► Managed supplier invoices, payments, and accounting registration
- ► Handled payment schedules and reclassification of advances, monitoring interim payments
- ► Developed a tool to track expenses and supplier payments, resulting in improved cash flow
- ► Established a supplier listing and budget monitoring using Power BI

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"[{project}]")