import streamlit as st
import pandas as pd     
import datetime as dt
import numpy as np
import plotly          
import plotly.express as px
import plotly.graph_objects as go
import altair as alt



st.title("Radiative Forcing")

""" @st.cache
def waterfallfig(df):
    fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = df['Measure'],
    x = df['Source'],
    textposition = "outside",
    text = df['Contribution'],
    y = df['Contribution'],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    return (fig)

st.plotly_chart(waterfallfig(df)) """

#factors = st.checkbox(df['Source'])

dff = pd.read_csv("yearlydata.csv")
#dff = dff[2:]
headers = dff.iloc[2]
new_df  = pd.DataFrame(dff.values[3:], columns=headers)

new_df = new_df.astype(float)
new_df['Year'] = new_df['Year'].astype(int)

new_df



@st.cache
def yearly_rf(year):
    thatyr = new_df['Year'] == year
    dfyear = new_df[thatyr]
    return dfyear

year = int(st.slider("Choose a year between 1850 and 2012", 1850, 2012))
st.write("You selected ", year)
data = yearly_rf(year)
#data

t = data[data.columns[1:]]
#t

bard = t.T
bard 

st.bar_chart(bard.values)

bard.index.name = 'newhead'
bard.reset_index(inplace=True)
bard['newhead'] = bard['newhead'].astype(str)
bard

bar = alt.Chart(bard).mark_bar().encode(
    x='newhead',
    y='19'
)
st.altair_chart(bar)

