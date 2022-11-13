import numpy as np
import pandas as pd
import streamlit as st
import csv

data = pd.read_csv('export.csv', delimiter=';', encoding='windows-1251')

data = pd.DataFrame(data)

with open('style.css') as f:
    st.markdown(f'<style> {f.read()}</style>',unsafe_allow_html=True)

data1 = data[data['claster_id'] == 0]
data2 = data[data['claster_id'] == 1]
data3 = data[data['claster_id'] == 2]
data4 = data[data['claster_id'] == 3]
data5 = data[data['claster_id'] == 4]


df1 = pd.DataFrame(
    data1,
    columns=['INN', 'claster_id'])

df2 = pd.DataFrame(
    data2,
    columns=['INN', 'claster_id'])

df3 = pd.DataFrame(
    data3,
    columns=['INN', 'claster_id'])

df4 = pd.DataFrame(
    data4,
    columns=['INN', 'claster_id'])

df5 = pd.DataFrame(
    data5,
    columns=['INN', 'claster_id'])

st.title('IP CLUSTER')

colbut1,colbut2,colbut3,colbut4,colbut5 = st.columns(5)
coldata, coldata1 = st.columns(2)

with colbut1:
    if st.button("Первый кластер"):
        with coldata:
            df = st.dataframe(df1, height=380) 
        with coldata1:
            st.bar_chart(df1, height=380)    
with colbut2:      
    if st.button("Второй кластер"):
        with coldata:
            df = st.dataframe(df2, height=380)  
        with coldata1:
            st.bar_chart(df2, height=380)   
with colbut3:
    if st.button("Третий кластер"):
        with coldata:
            df = st.dataframe(df3, height=380)
        with coldata1:
            st.bar_chart(df3, height=380)      
with colbut4:
    if st.button("Четвёртый кластер"):
        with coldata:
            df = st.dataframe(df4, height=380)
        with coldata1:
            st.bar_chart(df4, height=380)    
with colbut5:
    if st.button("Пятый кластер"):
        with coldata:
            df = st.dataframe(df5, height=380) 
        with coldata1:
            st.bar_chart(df5, height=380) 
