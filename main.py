import streamlit as st

from views import Pages



list_of_pages = [
    "About Project MabuhAI",
    "Demographics",
    "Factors and Profiling",
    "The Team"
]

st.sidebar.title(':scroll: Project MabuhAI')
st.sidebar.markdown('by Group Monty-Python | DSFC10')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "About Project MabuhAI":
    Pages.introduction()

elif selection == "Demographics":
    Pages.demog()

elif selection == "Factors and Profiling":
    Pages.show_factors_and_profile()

elif selection == "The Team":
    Pages.the_team()