import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
india=pd.read_csv('india.csv')
list_of_states=list(india['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India-2011')
selected_state=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select a Primary parameter',sorted(india.columns[5:]))
secondary=st.sidebar.selectbox('Select a Secondary parameter',sorted(india.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text(f'Size Represents {primary} ')
    st.text(f'Color Represents {secondary} ')

    if selected_state=='Overall India':
        fig = px.scatter_map(india, lat="Latitude", lon="Longitude",
                             color_continuous_scale=px.colors.cyclical.IceFire,size=primary,color=secondary, size_max=20, zoom=4,
                             map_style="carto-positron",hover_name='District',width=1800,height=700)
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df=india[india['State']==selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude",
                             color_continuous_scale=px.colors.cyclical.IceFire, size=primary, color=secondary,
                             size_max=20, zoom=6,
                             map_style="carto-positron",hover_name='District', width=1800, height=700)
        st.plotly_chart(fig, use_container_width=True)