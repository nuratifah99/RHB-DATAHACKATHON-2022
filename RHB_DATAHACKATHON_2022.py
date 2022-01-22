import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots 
import plotly.figure_factory as ff

# TITLE
st.set_page_config(page_title = 'RHB DataHackathon 2022',page_icon = "chart_with_upwards_trend",layout = 'wide')
title="Spending and Saving Plan"
# subtitle="RHB DataHackathon 2022 "
st.markdown(f"<h1 style='text-align: center; color: black;'>{title}</h1>",unsafe_allow_html=True)
# st.markdown(f"<h3 style='text-align: center; color: black;'>{subtitle}</h3>", unsafe_allow_html=True)
st.markdown("<hr/>",unsafe_allow_html=True) 

with st.expander("Car Insurance Calculator"):
    st.write('Coverage type: Comprehensive',unsafe_allow_html=False)
    choose1, choose2, choose3, choose4 = st.columns(4)
    
    with choose1:
        price = st.text_input('Car price (RM)',0)
        Car_price = int(price)
        
    with choose2:
        location = st.selectbox("Location",('West Malaysia', 'East Malaysia'))
        if location == 'West Malaysia':
            location = 'west_msia'
        elif location == 'East Malaysia':
            location = 'east_msia'
   
    with choose3:
        cc = st.selectbox("Engine Capacity",('1400', '1650', '2200', '3050', '4100', '4250', '4400', 'more than 4400' ))
        if cc == '1400':
            comprehensive_cover_west = 273.8
            comprehensive_cover_east = 196.2
        elif cc == '1650':
            comprehensive_cover_west = 305.5
            comprehensive_cover_east = 220    
        elif cc == '2200':
            comprehensive_cover_west = 339.1
            comprehensive_cover_east = 243.9
        elif cc == '3050':
            comprehensive_cover_west = 372.6
            comprehensive_cover_east = 266.5
        elif cc == '4100':
            comprehensive_cover_west = 404.3
            comprehensive_cover_east = 290.4
        elif cc == '4250':
            comprehensive_cover_west = 436
            comprehensive_cover_east = 313
        elif cc == '4400':
            comprehensive_cover_west = 469.6
            comprehensive_cover_east = 336.4
        elif cc == 'more than 4400':
            comprehensive_cover_west = 501.3
            comprehensive_cover_east = 359.5 
            
    with choose4:
        NCD = st.selectbox("No Claim Discount",('First year-25%', 'Second year-30%', 'Third year-38.33%', 'Fourth year-45%', 'Five year and more-55%'))
        if NCD == 'First year-25%':
            NCDval = 0.25
        elif NCD == 'Second year-30%':
            NCDval = 0.3
        elif NCD == 'Third year-38.33%':
            NCDval = 0.3833
        elif NCD == 'Fourth year-45%':
            NCDval = 0.45
        elif NCD == 'Five year and more-55%':
            NCDval = 0.55
    if location == 'west_msia':
        basic_premium=comprehensive_cover_west + 26*(Car_price-1000)/1000
    elif location == 'east_msia':
        basic_premium=comprehensive_cover_east + 20.3*(Car_price-1000)/1000
    less_NCD= NCDval*basic_premium
    Gross_premium=basic_premium-less_NCD
    
    st.markdown("<hr/>",unsafe_allow_html=True) 
    
    kpi1, kpi2 = st.columns(2)
    with kpi1:
        gross=str("{:.2f}".format(Gross_premium))
        st.markdown(f"<h4 style='text-align: center; color: black;'>{'Total payment'}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: black;'>{'RM ' + gross}</h3>", unsafe_allow_html=True)
        
    st.markdown("<vr/>",unsafe_allow_html=True)
    with kpi2:
        Monthly_goal=Gross_premium/12
        monthgoal=str("{:.2f}".format(Monthly_goal))
#         monthgoal=str(Monthly_goal)
        st.markdown(f"<h4 style='text-align: center; color: red;'>{'Monthly goal'}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: red;'>{'RM '+ monthgoal}</h3>", unsafe_allow_html=True)
        
    st.markdown("<hr/>",unsafe_allow_html=True) 
    
    if st.button('Set goal'):
        st.success('Your monthly goal has been set to RM '+ monthgoal)
      
    
with st.expander("Feature 2"):
    st.write('To be determined')
    
with st.expander("Feature 3"):
    st.write('To be determined')
    
st.markdown("<hr/>",unsafe_allow_html=True) 


    
