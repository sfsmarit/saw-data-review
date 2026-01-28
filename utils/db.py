import streamlit as st
from sfsaw import DataHandler

from . import tapeout as to
from .types import TapeoutSortKey


def list_parts() -> list[str]:
    parts = _load_parts()

    # Filter
    filter_key = st.session_state.get("filter_key", "")
    filter_val = st.session_state.get("filter_value", "")
    if filter_key and filter_val:
        parts = to.filter_parts(parts, by=filter_key, value=filter_val)  # type: ignore

    # Sort
    sort_key = st.session_state.get("sort_key", "")
    sort_asc = st.session_state.get("sort_ascending", False)
    if sort_key:
        parts = to.sort_parts(parts, by=sort_key, ascending=sort_asc)  # type: ignore

    return parts


def _load_parts() -> list[str]:
    handler = DataHandler()
    return handler.get_available_parts()


def build_handler(parts: list[str]) -> DataHandler:
    handler = DataHandler()
    with st.spinner("Loading data..."):
        for pn in parts:
            handler.load(pn, from_="db")
    return handler
