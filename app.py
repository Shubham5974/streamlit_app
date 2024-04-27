import pandas as pd
import streamlit as st

sheet_id = '1YNcK2HU-EmsskjWK0O5gt8fwCX8yqr2m7esPqCzJyuU'

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

st.write(df)