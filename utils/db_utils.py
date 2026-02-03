import streamlit as st
from sfsaw import DataHandler

from . import tapeout_utils as tapeut


def list_parts() -> list[str]:
    """
    List available part numbers, with filtering and sorting
    """
    parts = _load_parts()

    # Filter
    filter_conds = {
        "name": st.session_state.get("filter_pn", ""),
        "Application": st.session_state.get("filter_app", ""),
        "Bands": st.session_state.get("filter_band", ""),
        "LeadDesigner": st.session_state.get("filter_designer", ""),
    }
    for key, val in filter_conds.items():
        parts = tapeut.filter_parts(parts, by=key, value=val)  # type: ignore

    # Sort
    sort_key = st.session_state.get("sort_key", "")
    sort_asc = st.session_state.get("sort_ascending", False)
    if sort_key:
        parts = tapeut.sort_parts(parts, by=sort_key, ascending=sort_asc)  # type: ignore

    return parts


# @st.cache_data(ttl=60*10)
def _load_parts() -> list[str]:
    """Load available part numbers from the database"""
    handler = DataHandler()
    return handler.get_available_parts()


def build_handler(parts: list[str]) -> DataHandler:
    """Build a DataHandler by loading data for the given part numbers"""
    handler = DataHandler()
    with st.spinner("Loading data..."):
        for pn in parts:
            handler.load(pn, from_="db")
    return handler
