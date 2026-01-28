import streamlit as st
from sfsaw import plot

from utils import db


st.divider()
st.subheader("Frequency Trend")

# Part numbers
parts = st.multiselect(
    "Select Part Numbers",
    db.list_parts(),
)
if not parts:
    st.stop()


# Y data
y = st.segmented_control(
    "Plot data",
    ["PC2", "PWC", "FC2_RES1", "WC_RES1", "WC_df"],
)

if not y:
    st.stop()

# Load data
handler = db.build_handler(parts)


# Filter
handler.filter(column=y, exists=True)

# Plot
fig, ax = plot.trend(
    handler.df,
    y=y,
    height=5,
)
ax.set_ylabel(f"{y} [MHz]")
fig.tight_layout()
st.pyplot(fig, width="content")
