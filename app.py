import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI Career & Certification Advisor",
    page_icon="🎯",
    layout="centered"
)

knowledge_base = Path("knowledge_base.md").read_text(encoding="utf-8")

st.title("🎯 AI Career & Certification Advisor")
st.write(
    "A Creative Apps project built with GitHub Copilot. "
    "It uses a Foundry IQ-style grounded knowledge layer to provide career and certification guidance."
)

st.subheader("Tell me your background")

user_profile = st.text_area(
    "Example: I have PL-300 and AWS Cloud Practitioner. I come from a non-IT background and want to become a Data Analyst.",
    height=140
)

goal = st.selectbox(
    "Your target direction",
    [
        "Data Analyst",
        "BI Analyst",
        "Cloud / Azure Administrator",
        "AI / Data Project Portfolio",
        "Not sure yet"
    ]
)

if st.button("Generate Advice"):
    if not user_profile.strip():
        st.warning("Please enter your background first.")
    else:
        st.subheader("✅ Career Recommendation")

        st.markdown("### 1. Profile Summary")
        st.write(
            "You are building a career transition profile. Your certifications show foundation in data analytics and cloud awareness."
        )

        st.markdown("### 2. Strengths")
        strengths = []
        if "PL-300" in user_profile.upper() or "POWER BI" in user_profile.upper():
            strengths.append("Power BI / data visualisation foundation")
        if "AWS" in user_profile.upper():
            strengths.append("Basic cloud computing awareness")
        if "NON-IT" in user_profile.upper() or "non it" in user_profile.lower():
            strengths.append("Transferable business and workplace experience")

        if strengths:
            for item in strengths:
                st.write(f"- {item}")
        else:
            st.write("- Career motivation and willingness to learn through projects")

        st.markdown("### 3. Suggested Next Steps")
        if goal in ["Data Analyst", "BI Analyst"]:
            st.write("- Build one Power BI dashboard project using a public dataset")
            st.write("- Learn SQL fundamentals")
            st.write("- Practise explaining business insights from data")
            st.write("- Consider Microsoft Fabric / DP-600 after strengthening Power BI and data modelling")
        elif goal == "Cloud / Azure Administrator":
            st.write("- Learn Azure fundamentals and identity/networking basics")
            st.write("- Consider AZ-104 after practical Azure hands-on labs")
            st.write("- Build a small cloud portfolio project")
        elif goal == "AI / Data Project Portfolio":
            st.write("- Build an AI-assisted data insight app")
            st.write("- Add GitHub README, screenshots and architecture diagram")
            st.write("- Record a 2-minute demo video for interviews")
        else:
            st.write("- Start with a Data Analyst portfolio project")
            st.write("- Compare Data Analyst, BI Analyst and Cloud Admin job descriptions")
            st.write("- Identify repeated skills such as SQL, Power BI, Excel and Python")

        st.markdown("### 4. Project Idea for CV")
        st.write(
            "**AI Career & Certification Advisor** — an app that gives grounded career guidance "
            "based on certifications, target roles and learning goals."
        )

        st.markdown("### 5. Grounded Sources Used")
        st.info(
            "This answer is grounded using the local knowledge base in knowledge_base.md, "
            "representing the Foundry IQ concept of retrieval-grounded responses."
        )

        with st.expander("View knowledge base used"):
            st.markdown(knowledge_base)

st.divider()
st.caption("Hackathon project: Microsoft Agents League 2026 | Creative Apps Track | GitHub Copilot-assisted development")
