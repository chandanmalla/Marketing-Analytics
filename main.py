import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
# from autoviz.AutoViz_Class import AutoViz_Class
from scipy import stats  ## for KS test
from prettytable import PrettyTable
import plotly.express as px
import streamlit as st
combined_data = pd.read_csv('Combined_data.csv')

color = st.sidebar.selectbox("Select a Color:", [None,'Covid', 'City_Tier', 'Sale', 'WEEKDAY','Time_Month'])
facet_row = st.sidebar.selectbox("Select a facet_row:", [None,'Covid', 'City_Tier', 'Sale', 'WEEKDAY','Time_Month'])
facet_col = st.sidebar.selectbox("Select a facet_col:", [None,'Covid', 'City_Tier', 'Sale', 'WEEKDAY','Time_Month'])

fig = px.histogram(data_frame=combined_data, y=None, x='Log_Final Price', color=color,
    facet_row=facet_row, facet_col=facet_col,marginal='box',width=800, height=800 )
fig.update_layout(barmode = 'overlay')
fig.update_traces(opacity=0.70)
fig.update_layout(
    autosize=True,
    margin=dict(l=0, r=50, t=5, b=4  ),
)
#st.header("Distribution of Log_Final Price")
st.plotly_chart(fig)

