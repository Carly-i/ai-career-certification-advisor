# Architecture Diagram

```text
User
 |
 | enters background, certifications and career goal
 v
Streamlit Web App
 |
 | reads
 v
Local Knowledge Base (knowledge_base.md)
 |
 | grounded career and certification logic
 v
AI Career Recommendation Output
 |
 | displays:
 | - strengths
 | - skill gaps
 | - next steps
 | - project idea
 | - cited knowledge base
 v
User
