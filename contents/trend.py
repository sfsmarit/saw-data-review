import streamlit as st
from matplotlib import pyplot as plt
from sfsaw import plot

from utils import db


st.set_page_config("SAW Data Review", page_icon=":star:", layout="wide")


st.divider()
st.subheader("Trend")

# Part numbers
parts = st.multiselect(
    "Select part numbers",
    db.list_parts(),
)
if not parts:
    st.stop()


# Y data
y = st.segmented_control(
    "Plot data",
    ["scanspeed", "WC_df", "PWC", "PC2", "WC_RES1", "FC2_RES1"],
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

if y == "scanspeed":
    ax.set_yscale("log")
    ax.get_yaxis().set_major_formatter(plt.ScalarFormatter())  # type: ignore
    ax.set_ylim(7, 500)
    ax.set_yticks([8, 10, 20, 30, 40, 60, 80, 100, 150, 200, 300, 500])

fig.tight_layout()
st.pyplot(fig, width="content")
