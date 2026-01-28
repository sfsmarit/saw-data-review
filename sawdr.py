import streamlit as st


st.set_page_config("SAW Data Review", page_icon=":star:", layout="wide")
st.title("SAW Data Review")

pages = [
    st.Page("contents/freq_trend.py", title="Freq trend")
]

st.navigation(pages).run()
