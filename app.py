import streamlit as st
import pymysql
import pandas as pd

# -------------------------------
# Page Configuration & Styling
# -------------------------------
st.set_page_config(
    page_title="Intelligent Candidate Ranking Engine",
    layout="wide",
    page_icon="🎯"
)

# Custom CSS to tweak spacing, borders, and metric styling
# FIXED: Changed 'unsafe_with_html' to the correct 'unsafe_allow_html'
st.markdown("""
    <style>
    .metric-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #483D8B;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div[data-testid="stMetric"] {
        background-color: rgba(240, 242, 246, 0.5);
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Intelligent Candidate Ranking Engine")
st.caption("Streamlined talent discovery, assessment, and automatic placement analytics.")
st.write("---")

# -------------------------------
# Database Connection & Caching
# -------------------------------
@st.cache_data(ttl=600)
def load_data():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="nandu",
        database="candidate_ranking"
    )
    query = """
    SELECT *
    FROM candidates
    ORDER BY rank_position;
    """
    try:
        df = pd.read_sql(query, connection)
    finally:
        connection.close()
    return df

df = load_data()

# -------------------------------
# Sidebar: Job Description & Controls
# -------------------------------
with st.sidebar:
    st.header("📋 Job Description")
    try:
        with open("job_description.txt", "r", encoding="utf-8") as file:
            jd = file.read()
        st.info(jd)
    except FileNotFoundError:
        st.warning("⚠️ 'job_description.txt' not found.")
    
    st.write("---")
    st.subheader("⚙️ System Controls")
    
    if st.button("🔄 Refresh & Clear Cache", use_container_width=True, type="primary"):
        st.cache_data.clear()
        st.rerun()

# -------------------------------
# Dashboard Metrics
# -------------------------------
if not df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Candidates Evaluated", value=f"{len(df)} profiles")
    with col2:
        max_score = df["score"].max() if "score" in df.columns else 0
        st.metric(label="Highest Benchmark Score", value=f"{max_score} pts")
    with col3:
        top_cand = df.iloc[0]["name"] if "name" in df.columns else "N/A"
        st.metric(label="Top Ranked Candidate", value=str(top_cand))
    
    st.write("---")

    # -------------------------------
    # Candidate Ranking Table
    # -------------------------------
    st.subheader("🏆 Master Candidate Rankings")
    
    desired_cols = ["rank_position", "name", "degree", "branch", "experience", "score"]
    available_cols = [col for col in desired_cols if col in df.columns]
    
    # Styled dataframe with streamlined column names and specific configurations
    st.dataframe(
        df[available_cols], 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "rank_position": st.column_config.NumberColumn("Rank", format="#%d"),
            "name": "Full Name",
            "degree": "Degree",
            "branch": "Branch/Specialization",
            "experience": st.column_config.NumberColumn("Experience", format="%d Years"),
            "score": st.column_config.ProgressColumn("Match Score", min_value=0, max_value=100, format="%d pts")
        }
    )
    st.write("---")

    # -------------------------------
    # Search & Select Segment
    # -------------------------------
    col_search, col_select = st.columns(2)

    with col_search:
        with st.container(border=True):
            st.markdown("### 🔍 Real-time Candidate Search")
            search = st.text_input("Type any part of a candidate's name:", placeholder="e.g. John Doe")
            
            if search:
                result = df[df["name"].str.contains(search, case=False, na=False)]
                if not result.empty:
                    st.dataframe(result[available_cols], use_container_width=True, hide_index=True)
                else:
                    st.error("No matches found.")

    with col_select:
        with st.container(border=True):
            st.markdown("### 🎯 Interactive Profile Viewer")
            selected_candidate = st.selectbox(
                "Select a candidate to view their complete portfolio:",
                options=df["name"].unique()
            )

    # -------------------------------
    # Deep-Dive Candidate Profile 
    # -------------------------------
    if selected_candidate:
        candidate = df[df["name"] == selected_candidate].iloc[0]
        
        st.write("##") # Spacer
        
        # Profile Summary Header Card
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"# 👤 {candidate['name']}")
                st.caption(f"{candidate.get('degree', 'Degree')} in {candidate.get('branch', 'Branch')}")
            with c2:
                st.metric(label="System Position", value=f"Rank #{candidate.get('rank_position', 'N/A')}")
            
            st.write("---")
            
            # Detailed Breakdown columns
            p_col1, p_col2 = st.columns(2)
            
            with p_col1:
                st.markdown("### 📇 Personal & Contact Information")
                
                details = {
                    "💼 Professional Experience": f"{candidate.get('experience', '0')} Years",
                    "🏛️ College/University": candidate.get("college", None),
                    "📊 Current CGPA": candidate.get("cgpa", None),
                    "📈 Aggregate Percentage": candidate.get("percentage", None),
                    "📧 Email Address": candidate.get("email", None),
                    "📞 Phone Number": candidate.get("phone", None),
                    "🌐 LinkedIn Profile": candidate.get("linkedin", None),
                    "💻 GitHub Repository": candidate.get("github", None)
                }
                
                for label, value in details.items():
                    if value and pd.notna(value):
                        st.write(f"**{label}:** {value}")

            with p_col2:
                st.markdown("### 🛠️ Evaluation & Core Competencies")
                
                tech_details = {
                    "🚀 Core Skills": candidate.get("skills", None),
                    "📂 Key Projects": candidate.get("projects", None),
                    "🏢 Past Internships": candidate.get("internships", None),
                    "📜 Certifications": candidate.get("certifications", None),
                    "🏅 Major Achievements": candidate.get("achievements", None),
                    "🗣️ Languages Known": candidate.get("languages_known", None)
                }
                
                for label, value in tech_details.items():
                    if value and pd.notna(value):
                        st.write(f"**{label}:** {value}")
                
                st.write("---")
                # Safeguard progress bar rendering by casting numerical data properly
                try:
                    score_val = int(candidate.get('score', 0))
                except (ValueError, TypeError):
                    score_val = 0
                    
                st.progress(score_val / 100.0)
                st.success(f"📈 **Match Compatibility:** {score_val}% matching criteria achieved.")

else:
    st.warning("📋 No candidate profiles detected. Verify your MySQL `candidates` database configuration.")