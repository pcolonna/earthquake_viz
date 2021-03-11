import streamlit as st
import dataset

st.set_page_config(layout="wide")

st.title("Earthquake Viz")

data = dataset.build()
st.map(data)