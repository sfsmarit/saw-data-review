import streamlit as st
from sfsaw import plot
from utils import db


st.set_page_config("SAW Data Review", page_icon=":star:", layout="centered")

st.subheader("Map")

# Part number
part = st.selectbox(
    "Select part number",
    db.list_parts(),
)
if not part:
    st.stop()

# Build handler
handler = db.build_handler([part])

# Wafer
wafer = st.selectbox(
    "Select wafer",
    handler.wafers,
)
if not wafer:
    st.stop()

# Y data
z = st.segmented_control(
    "Plot data",
    ["scanspeed", "WC_df", "PWC", "PC2", "WC_RES1", "FC2_RES1"],
)
if not z:
    st.stop()

# Filter
handler.filter(column=z, exists=True)

# Plot
fig, ax = plot.heatmap(
    handler.df,
    wafer,
    z=z
)
st.pyplot(fig, width="content")
