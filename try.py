import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()
st.sidebar.title('Flights Analytics')
user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])
