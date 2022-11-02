#Import Python Libraries
import matplotlib.pyplot as plt
import numpy as np
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
import pandas as pd
import numpy as np
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import folium
import branca



@st.cache
def read_csv(path):
    return pd.read_csv(path)
     
#Data prepartion to only retrieve fields that are relevent to this project
dre=read_csv("drought_spain_table.csv")
dre['1.5°C']=pd.to_numeric(dre['1.5°C'].astype(str).str.replace(',',''))
dre['2.0°C']=pd.to_numeric(dre['2.0°C'].astype(str).str.replace(',',''))
dre['3.0°C']=pd.to_numeric(dre['3.0°C'].astype(str).str.replace(',',''))
dre['4.0°C']=pd.to_numeric(dre['4.0°C'].astype(str).str.replace(',',''))
fig=make_subplots(specs=[[{"secondary_y":True}]])

fig.add_trace(                           #Add a bar chart to the figure
        go.Bar(
        x=dre['scenarios'],
        y=dre['1.5°C'],
        name="economic loss",
        hoverinfo='none'                 #Hide the hoverinfo
        ),
        secondary_y=False)  
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=0.7,
            y=1.2,
            showactive=True,
            buttons=list(
                [
                    dict(
                        label="1.5",
                        method="update",
                        args=[{"y": [dre['1.5°C'],dre['scenarios']]}],
                    ),
                    dict(
                        label="2",
                        method="update",
                        args=[{"y": [dre['2.0°C'],dre['scenarios']]}],
                    ),
                ]
            ),
        )
    ]
)

def app():
    st.title('Projected economic impact(bn euros)')
    st.write("Economic loss in different scenarios from a global wearming level of 1.5°C or 2°C in Spain")
    st.plotly_chart(fig)
