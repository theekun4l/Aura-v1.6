import streamlit as st

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

aura = st.Page(
    "pages/aura.py",
    title="Aura",
    icon="🤖"
)

manager = st.Page(
    "pages/manager_page.py",
    title="Manager",
    icon="📁"
)

pg = st.navigation(
    [home, aura,  manager],
    position="hidden"
)

pg.run()