# Deploy Price Predictor

# ======================================================
import pandas as pd
import numpy as np

from xgboost.sklearn import XGBRegressor
import streamlit as st
import pickle


# ======================================================

# Judul Utama
st.write('''
# DAEGU APARTEMENT PRICE PREDICTOR
''')

# sidebar
st.sidebar.header("Please input apartement's features")


# ======================================================

# buat function untuk user input feature
def user_input_feature():

    # st.sidebar.slider('label', min, mav, value)
    # st.sidebar.selectbox('label', (cat1,cat2,cat3))

    # numerical: slider atau number input
    N_FacilitiesNearBy_ETC = st.sidebar.number_input('N_FacilitiesNearBy_ETC', min_value=0, max_value=5, value=1, step=1)
    N_FacilitiesNearBy_PublicOffice = st.sidebar.number_input('N_FacilitiesNearBy_PublicOffice', min_value=0, max_value=7, value=1, step=1)
    N_SchoolNearBy_University = st.sidebar.number_input('N_SchoolNearBy_University', min_value=0, max_value=5, value=1, step=1)
    N_Parkinglot = st.sidebar.number_input('N_Parkinglot_Basement', min_value=0, max_value=1321, value=1, step=1)
    N_FacilitiesInApt = st.sidebar.number_input('N_FacilitiesInApt', min_value=1, max_value=10, value=1, step=1)
    YearBuilt = st.sidebar.number_input('YearBuilt', min_value=1978, max_value=2023, value=2010, step=1)
    Size_sqf = st.sidebar.number_input('Size_sqf', min_value=135, max_value=2337, value=1000, step=1)

    # categorical : selecbox 
    HallwayType = st.sidebar.selectbox('HallwayType', ('terraced', 'mixed', 'corridor'))
    TimeToSubway = st.sidebar.selectbox('TimeToSubway', ('0-5min', '10-15min', '15-20min', '5-10min', 'no_bus_stop_nearby'))
    SubwayStation = st.sidebar.selectbox('SubwayStation', ('Kyungbuk-uni-hospital', 'Chil-sung-market', 'Bangoge', 'Sin-nam',
       'Banwoldang', 'no_subway_nearby', 'Myung-duk', 'Daegu'))

    df = pd.DataFrame()
    df['N_FacilitiesNearBy(ETC)'] = [N_FacilitiesNearBy_ETC]
    df['N_FacilitiesNearBy(PublicOffice)'] = [N_FacilitiesNearBy_PublicOffice]
    df['N_SchoolNearBy(University)'] = [N_SchoolNearBy_University]
    df['N_Parkinglot(Basement)'] = [N_Parkinglot]
    df['N_FacilitiesInApt'] = [N_FacilitiesInApt]
    df['YearBuilt'] = [YearBuilt]
    df['Size(sqf)'] = [Size_sqf]
    df['HallwayType'] = [HallwayType]
    df['TimeToSubway'] = [TimeToSubway]
    df['SubwayStation'] = [SubwayStation]

    return df

df_customer = user_input_feature()
df_customer.index = ['value']

# predict a customer
model_loaded = pickle.load(open('model_xgboost_Anastasia.sav','rb'))

price = model_loaded.predict(df_customer)


# ======================================================

# buat 2 container di kiri dan kanan
col1, col2 = st.columns(2)

# bagian kiri (col1)
with col1:
    # Tampilkan dataframe hasil user input (customer feature)
    st.subheader("Apartement Features:")
    st.write(df_customer.transpose())


# bagian kanan (col2)
with col2:
    # Tampilkan hasil prediksi
    st.subheader("Price Prediction")
    st.write(price)
