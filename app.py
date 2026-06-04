import streamlit as st
import pandas as pd

from data_profiler_dashboard.profiler import (
    get_column_profile,
    get_dataset_summary,
)


st.set_page_config(
    page_title="Data Profiler Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Data Profiler Dashboard")

st.write(
    "Upload a CSV or Parquet file to generate a quick profiling summary."
)

uploaded_file = st.file_uploader(
    "Choose a CSV or Parquet file",
    type=["csv", "parquet"],
)

if uploaded_file is None:
    st.info("Upload a file to get started.")
    st.stop()

if uploaded_file.name.endswith(".csv"):
    dataframe = pd.read_csv(uploaded_file)
elif uploaded_file.name.endswith(".parquet"):
    dataframe = pd.read_parquet(uploaded_file)
else:
    st.error("Unsupported file type.")
    st.stop()

st.subheader("Data Preview")
st.dataframe(dataframe.head(20), use_container_width=True)

st.subheader("Dataset Summary")
summary = get_dataset_summary(dataframe)

col1, col2, col3 = st.columns(3)
col1.metric("Rows", summary["row_count"])
col2.metric("Columns", summary["column_count"])
col3.metric("Duplicate Rows", summary["duplicate_row_count"])

st.subheader("Column Profile")
column_profile = get_column_profile(dataframe)
st.dataframe(column_profile, use_container_width=True)

csv_report = column_profile.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download column profile as CSV",
    data=csv_report,
    file_name="column_profile.csv",
    mime="text/csv",
)