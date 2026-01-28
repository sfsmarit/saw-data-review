import streamlit as st
from typing import get_args
import os
import json

from utils.types import TapeoutSortKey, TapeoutFilterKey

if os.name == "nt":
    SUMMARY_FILE = "tmp/summary.json"
else:
    SUMMARY_FILE = "/data/skyfoundry/output/summary.json"


@st.cache_data(ttl=60*5)
def load_summary():
    with open(SUMMARY_FILE, "r") as f:
        return json.load(f)


def tapeout_name(part_number: str) -> str:
    return part_number[:5] + "-" + part_number[5] + "-OSK"


def sort_keys() -> list[str]:
    return list(get_args(TapeoutSortKey))


def filter_keys() -> list[str]:
    return list(get_args(TapeoutFilterKey))


def sort_parts(part_numbers: list[str],
               by: TapeoutSortKey,
               ascending: bool = False) -> list[str]:
    summary = load_summary()

    if by == "name":
        return sorted(part_numbers, reverse=not ascending)
    elif by == "ScheduledTapeOutDate":
        def key_func(pn: str):
            date = summary.get(tapeout_name(pn), {}).get(by, "2000/01/01")
            return date.replace("/", "")
        return sorted(part_numbers, key=key_func, reverse=not ascending)


def filter_parts(part_numbers: list[str],
                 by: TapeoutFilterKey,
                 value: str) -> list[str]:
    summary = load_summary()

    if by == "name":
        return [pn for pn in part_numbers if value.lower() in pn.lower()]
    else:
        return [pn for pn in part_numbers if value.lower() in summary.get(tapeout_name(pn), {}).get(by).lower()]
