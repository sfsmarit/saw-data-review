import streamlit as st
from utils import tapeout as to


st.title("SAW Data Review")


# Sidebar
st.sidebar.text("Filter")
st.sidebar.selectbox(
    "Key", to.filter_keys(), key="filter_key"
)
st.sidebar.text_input("Value", key="filter_value")

st.sidebar.divider()

st.sidebar.text("Sort")
st.sidebar.selectbox(
    "Key", to.sort_keys(), index=1, key="sort_key"
)
st.sidebar.toggle("Ascending", False, key="sort_ascending")


# Main pages
pages = [
    st.Page("contents/trend.py", title="Trend"),
    st.Page("contents/map.py", title="Map"),
]

st.navigation(pages).run()
