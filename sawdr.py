import streamlit as st
from utils import tapeout_utils as tapeut


st.title("SAW Data Review")


# Sidebar
st.sidebar.text("Filter")
st.sidebar.text_input("Part Number", key="filter_pn")
st.sidebar.segmented_control("", ["Duplexer", "Filter"], key="filter_app", label_visibility="collapsed")
st.sidebar.text_input("Band", key="filter_band")
st.sidebar.text_input("Designer", key="filter_designer")

st.sidebar.divider()

st.sidebar.text("Sort")
st.sidebar.selectbox(
    "Key", tapeut.sort_keys(), index=1, key="sort_key"
)
st.sidebar.toggle("Ascending", False, key="sort_ascending")


# Main pages
pages = [
    st.Page("contents/trend.py", title="Trend", icon=":material/trending_up:"),
    st.Page("contents/map.py", title="Map", icon=":material/stop_circle:"),
    st.Page("contents/develop.py", title="Develop", icon=":material/settings:"),
]

st.navigation(pages).run()
