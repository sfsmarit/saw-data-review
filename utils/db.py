import streamlit as st
from sfsaw import DataHandler


@st.cache_resource
def list_parts():
    handler = DataHandler()
    return handler.get_available_parts()


@st.cache_data(ttl=60*5)
def build_handler(parts: list[str]) -> DataHandler:
    handler = DataHandler()
    with st.spinner("Loading data..."):
        for pn in parts:
            handler.load(pn, from_="db")
    return handler
