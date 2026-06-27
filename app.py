import streamlit as st
import pymysql
import pandas as pd

# -------------------------------
# Database Connection
# -------------------------------

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="nandu",
    database="candidate_ranking"
)

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Intelligent Candidate Ranking Engine",
    layout="wide"
)

st.title("🎯 Intelligent Candidate Ranking Engine")

# -------------------------------
# Read Data from MySQL
# -------------------------------

query = """
SELECT *
FROM candidates
ORDER BY rank_position;
"""

df = pd.read_sql(query, connection)

# -------------------------------
# Dashboard Metrics
# -------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Candidates", len(df))

with col2:
    st.metric("Highest Score", df["score"].max())

with col3:
    st.metric("Top Candidate", df.iloc[0]["name"])

st.divider()

# -------------------------------
# Candidate Ranking Table
# -------------------------------

st.subheader("🏆 Candidate Ranking")

st.dataframe(
    df[
        [
            "rank_position",
            "name",
            "degree",
            "branch",
            "experience",
            "score"
        ]
    ],
    use_container_width=True
)

st.divider()

# -------------------------------
# Search Candidate
# -------------------------------

search = st.text_input("🔍 Search Candidate")

if search:

    result = df[df["name"].str.contains(search, case=False)]

    st.dataframe(result, use_container_width=True)

st.divider()

# -------------------------------
# Select Candidate
# -------------------------------

selected_candidate = st.selectbox(

    "Select Candidate",

    df["name"]

)

candidate = df[df["name"] == selected_candidate]

st.header("📄 Candidate Details")

st.write("### Personal Details")

st.write("**Name :**", candidate["name"].values[0])

st.write("**Degree :**", candidate["degree"].values[0])

st.write("**Branch :**", candidate["branch"].values[0])

st.write("**Experience :**", candidate["experience"].values[0])

if "college" in df.columns:
    st.write("**College :**", candidate["college"].values[0])

if "cgpa" in df.columns:
    st.write("**CGPA :**", candidate["cgpa"].values[0])

if "percentage" in df.columns:
    st.write("**Percentage :**", candidate["percentage"].values[0])

st.divider()

st.write("### Technical Details")

if "skills" in df.columns:
    st.write("**Skills :**", candidate["skills"].values[0])

if "projects" in df.columns:
    st.write("**Projects :**", candidate["projects"].values[0])

if "internships" in df.columns:
    st.write("**Internships :**", candidate["internships"].values[0])

if "certifications" in df.columns:
    st.write("**Certifications :**", candidate["certifications"].values[0])

if "achievements" in df.columns:
    st.write("**Achievements :**", candidate["achievements"].values[0])

if "languages_known" in df.columns:
    st.write("**Languages :**", candidate["languages_known"].values[0])

st.divider()

st.write("### Contact Details")

if "email" in df.columns:
    st.write("**Email :**", candidate["email"].values[0])

if "phone" in df.columns:
    st.write("**Phone :**", candidate["phone"].values[0])

if "linkedin" in df.columns:
    st.write("**LinkedIn :**", candidate["linkedin"].values[0])

if "github" in df.columns:
    st.write("**GitHub :**", candidate["github"].values[0])

st.divider()

st.write("### Ranking")

st.success(f"⭐ Score : {candidate['score'].values[0]}")

st.success(f"🏅 Rank : {candidate['rank_position'].values[0]}")

# -------------------------------
# Job Description Sidebar
# -------------------------------

with open("job_description.txt", "r") as file:

    jd = file.read()

st.sidebar.title("📋 Job Description")

st.sidebar.write(jd)

# -------------------------------
# Refresh Button
# -------------------------------

if st.button("🔄 Refresh Dashboard"):

    st.rerun()

# -------------------------------
# Close Connection
# -------------------------------

connection.close()
