import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="My Projects", layout="wide")
st.title("My Projects")

root = Path(__file__).parent / "html_projects"
root.mkdir(exist_ok=True)

projects = sorted(p for p in root.iterdir() if (p / "index.html").exists())

if not projects:
    st.info("No projects yet. Add a folder with an index.html inside html_projects/")
else:
    choice = st.selectbox(
        "Choose a project",
        projects,
        format_func=lambda p: p.name,
        key="html_project_picker",
    )
    html = (choice / "index.html").read_text(encoding="utf-8")
    components.html(html, height=700, scrolling=True)
