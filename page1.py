import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Nazvanie
st.title('My 1st DS APP')

ts = 'GOOGL'
td = yf.Ticker(ts)
tdf = td.history(period='1d', start='2010-5-31', end='2024-5-31')
activated = st.toggle('Развернуть')
if activated:
    st.write('Данные о котировках компании Apple',tdf)
else:
    st.write('Данные о котировках компании Apple',tdf.head(10))
st.sidebar.write('Нарисовать графики')
button1 = st.sidebar.button('Open график')
if button1:
    g1 = st.area_chart(tdf.Open)
button2 = st.sidebar.button('High график')   
if button2:
    g2 = st.area_chart(tdf.High)
button3 = st.sidebar.button('Low график')   
if button3:
    g3 = st.area_chart(tdf.Low)
button4 = st.sidebar.button('Close график')   
if button4:
    g4 = st.area_chart(tdf.Close)
button5 = st.sidebar.button('Volume график')
if button5:
    g5 = st.area_chart(tdf.Volume)
button6 = st.sidebar.button('Все графики')
if button6:
    st.write('Open график')
    st.line_chart(tdf.Open)
    st.write('High график')
    st.line_chart(tdf.High)
    st.write('Low график')
    st.line_chart(tdf.Low)
    st.write('Close график')
    st.line_chart(tdf.Close)
    st.write('Volume график')
    st.line_chart(tdf.Volume)
st.sidebar.write('Скачать файлы')
dw_button = st.sidebar.download_button(label='Скачать CSV-файл', data=tdf.to_csv(), file_name='AppleCot.csv')
