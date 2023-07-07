from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = str(current_dir / "Styles" / "main.css")
resume_file = str(current_dir / "Assets" / "CV.pdf")
profile_pic = str(current_dir / "Assets" / "profile-pic.jfif")


# --------- GENERAL SETTINGS -----------

PAGE_TITLE = "My digital CV | Emmanuel G."
PAGE_ICON = ":wave:"
NAME = "I am Emmanuel Gakosso"
DESCRIPTION = """
Data analyst in apprenticeship for more than 3 years now, assisting financial auditors by supporting data-driven decision-making and apart from that, Alteryx communities contributor.
"""
EMAIL = "emmanuelgakosso3@gmail.com"
PHONE_NUMBER = "+33 6 24 26 57 29"
SOCIA_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/emmanuel-gakosso/",
    "Alteryx Profile":"https://community.alteryx.com/t5/user/viewprofilepage/user-id/228436",
    "Dataiku DSS Profile":"https://accounts.skilljar.com/accounts/profile/2uefx9200kvpn?d=2uefx9200kvpn&next=%2F",
    "GitHub":"https://github.com/Emmanuel558"
}

PROJECTS = {
    "Bar-Chart-Race - Chronological evolution of the covid19 figures via an interactive and autonomous video produced with Python and Alteryx for the repatriation of data and the related processing.":"https://github.com/Emmanuel558/Alteryx",
    "KMeans Segmentation of clients":"https://github.com/Emmanuel558/Alteryx",
    "Visual analysis of financial forecasts and achievement of budget and management objectives on Power BI":"https://github.com/Emmanuel558/Alteryx/blob/main/Analyse%20budgets%20et%20r%C3%A9sultats.pbix",
    "Analysis and evaluation of hotel levels for an apartment manager and mapping on power BI":"https://github.com/Emmanuel558/Alteryx/blob/main/Evaluation%20des%20%C3%A9tablissements.pbix",
    "Web scraping and data analysis":"https://github.com/Emmanuel558/Web-scraping-and-reporting"
}

CERTIFICATIONS = {
    "Alteryx Core certified":"https://www.credly.com/badges/57cd79a4-4bf3-47b5-b29a-3c79c0eaf672/linked_in_profile",
    "Alteryx Advanced certified":"https://www.credly.com/badges/b62a27c6-6528-4409-aa43-8657bbce5c98?source=linked_in_profile",
    "Microsoft Power-BI Data Analyst Associate":"https://drive.google.com/file/d/1GY4gAXhogbhPHWKNdx3SYwAFnqZXN9sC/view?usp=drive_link",
    "Data Wrangling and Prep on Trifacta Cloud Platform":"https://www.credly.com/badges/ad913d78-8ac5-4276-bb7a-cdacf6bb4d5c?source=linked_in_profile",
    "Dataiku core certified":"https://verify.skilljar.com/c/fepmkaorxhyj",
    "Dataiku Advanced certified":"https://verify.skilljar.com/c/7qvocvv32jvg",
    "Dataiku Machine Learning Practitionner":"https://verify.skilljar.com/c/gyjnajcz9omj",
    "Most complimented author and top 3 problem solvers in the French-speaking community of alteryx during the 2nd quarter of 2022":"https://community.alteryx.com/t5/Blog-Francais/Top-Contributeurs-amp-certifies-Q2-2022/ba-p/962917",
    "Finalist of a competition organized by members of the Alteryx community in Paris":"https://community.alteryx.com/t5/Paris-FR-Francais/Resume-du-Alteryx-User-Group-de-Paris-T4-2021/m-p/848635#M231",
    "Successful completion of the assessment of advanced T-SQL on HackerRank":"https://www.hackerrank.com/certificates/77a7179a9209?utm_medium=email&utm_source=mail_template_1393&utm_campaign=hrc_skills_certificate",
    "Top contributor in Alteryx French community in 2022":"https://community.alteryx.com/t5/Blog-Francais/Top-contributeurs-2022/ba-p/1063302?emcs_t=S2h8ZW1haWx8bWVudGlvbl9zdWJzY3JpcHRpb258TENSS1FZRk9MWVc2R1h8MTA2MzMwMnxBVF9NRU5USU9OU3xoSw"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.header("Hi! Welcome on my profile. 😀")

# ---------- LOAD CSS, PDF & PROFILE PIC ---------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ------ HERO SECTION -------

col1, col2 = st.columns(2)

with col1:

    st.image(profile_pic, width=230)

with col2:

    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resume",
        data = PDFbyte,
        file_name = resume_file,
        mime = "application/octet-stream"
    )

    st.write("Email address: "+EMAIL)
    st.write("Phone number: " + PHONE_NUMBER)


# ------ SOCIAL LINKS -------

st.write("#")
cols = st.columns(len(SOCIA_MEDIA))

for index, (platform, link) in enumerate(SOCIA_MEDIA.items()):

    cols[index].write(f"[{platform}]({link})")

# ---- EXPERIENCES & QUALIFICATIONS ------

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    f"""
    For more than 3 years now within the Data & Analytics team of KPMG France, my daily tasks are:
    
-  {chr(0x2705)}Optimizing data analytics pipelines for automating defined and undefined data reprocessing from multiple ERPs on Alteryx;
-  {chr(0x2705)}Supervision and training of auditors on the ETL by communicating knowledge on best practices in the context of the use of Alteryx and Power BI;
-  {chr(0x2705)}Analysis of accounting entries and reliability of ledger data from different ERPs for framing with balance;
-  {chr(0x2705)}Analysis of cash flow and turnover,
-  {chr(0x2705)}Improved performance and runtime of workflows in Alteryx Designer;
-  {chr(0x2705)}Active contributor to the French-speaking Alteryx France community.
    """
)

# ----- SKILLS ----

st.write("#")
st.subheader("Hard skills")
st.write(
    f"""
-  {chr(0x1F4DA)}Programming and ETL : Python (Basics, Pandas, numpy, scikit-learn, streamlit), Alteryx, Dataiku DSS, Trifacta Cloud\n
-  {chr(0x1F4CA)}Data visualization : PowerBI, Excel, Dataiku, Plotly, Seaborn, Google Data Studio
-  {chr(0x1F4BB)}Modeling : Excel solver, Logistic regression, linear regression, decision trees, K-Nearest-Neighbours, KMeans
    """
)

# --------- Projects, Accomplishments & Certifications ------

st.write("#")
st.subheader("Some projects")
st.write("----")

for project, link in PROJECTS.items():
    st.write(f"[{chr(0x1F6A7)}{project}]({link})")

st.write("#")
st.subheader("Certifications & some accomplishments")
st.write("----")

for certification, link in CERTIFICATIONS.items():
    st.write(f"[{chr(0x1F3C6)}{certification}]({link})")
