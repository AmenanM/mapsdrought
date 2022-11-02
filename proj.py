#Import Python Libraries
import pandas as pd
import folium 
from folium.features import GeoJsonPopup, GeoJsonTooltip
import streamlit as st
from streamlit_folium import folium_static
import numpy as np
import plotly
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import folium
import branca
import streamlit.components.v1 as components


@st.cache
def read_csv(path):
    return pd.read_csv(path)
     
#Data prepartion to only retrieve fields that are relevent to this project
spain_data2=read_csv("dr2.csv")

time_index = list(spain_data2['year'].sort_values().astype('str').unique())
import folium
from folium import plugins
from folium.plugins import HeatMapWithTime
import branca.colormap as cm
import branca
from branca.element import Element, Figure, Html, MacroElement
from collections import defaultdict
data = []
for _, d in spain_data2.groupby('year'):
    data.append([[row['lat'], row['lon'], row['indices']] for _, row in d.iterrows()])
data
m= folium.Map(location=[spain_data2.lat.mean(),spain_data2.lon.mean()],zoom_start=5,
             tiles='cartodbpositron')
HeatMapWithTime(data,
                index=time_index,
                auto_play=True,
                use_local_extrema=True
               ).add_to(m)
# n
# colors = ['blue', 'lime', 'red']
# vmin = 0
# vmax = 10000
folium.Marker([41.39, 2.15], 
              popup='asset',
              icon=folium.Icon(color='red',icon='university', prefix='fa') 
             ).add_to(m)
steps=20
colormap = branca.colormap.linear.YlOrRd_09.scale(spain_data2['indices'].min(), 
spain_data2['indices'].max()).to_step(steps)
gradient_map=defaultdict(dict)
for i in range(steps):
    gradient_map[1/steps*i] = colormap.rgb_hex_str(1/steps*i)
colormap.add_to(m)


# app1.py
import streamlit as st
def app():
    st.title('projection')
    st.write("Visualize historial series and projected values of the SPEI drought indexes for Spain.We have 5 classes, namely: 1- Non-Drought (in this class the value of SPEI greater than -0.5), 2- Mild (the value of SPEI is between -0.5 and -1), 3- Moderate (SPEI is between -1.5 and -1), 4- Severe (SPEI is between -2 and -1.5), and 5- Extreme (Less than -2).")
    st.write(spain_data2)  
    folium_static(m)

