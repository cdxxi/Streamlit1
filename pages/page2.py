import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import numpy as np

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['time_order'] = np.random.choice((pd.date_range(start='2023-01-01', end='2023-01-31')), size=len(tips))

st.title('My 2nd DS APP')
uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    activated = st.toggle('Развернуть')
    if activated:
        st.write('Ваш ДатаФрейм',df)
    else:
        st.write('Ваш ДатаФрейм',df.head(10))

choise = st.selectbox('Варианты отображения', ['первые 10 строк', 'последние 10 строк', 'весь датафрейм'])
if choise == 'первые 10 строк':
    st.write(tips.head(10))
elif choise =='последние 10 строк':
    st.write(tips.tail(10))
else:
    st.write(tips)

button1 = st.sidebar.button('График динамики чаевых')
if button1:
    fig = plt.figure(figsize=(12,5))
    ax = sns.lineplot(x='time_order', y='tip', data=tips)
    ax.set_title('График динамики чаевых')
    ax.set_xlabel('дата')
    ax.set_ylabel('Чаевые')
    st.pyplot(fig)
    plt.savefig('1.png')
    with open("1.png", 'rb') as file:
        dw = st.sidebar.download_button(label="Скачать график", data=file, file_name="1.png", mime="image/png")

button2 = st.sidebar.button('График размера счета')
if button2:
    fig = plt.figure(figsize=(12,5))
    ax = sns.histplot(tips['total_bill'])
    ax.set_title('Размер счета')
    ax.set_xlabel('Размер')
    ax.set_ylabel('Количество раз')
    st.pyplot(fig)
    plt.savefig('2.png')
    with open("2.png", 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='2.png', mime='image/png' )

button3 = st.sidebar.button('График размера счета и чаевых')
if button3:
    fig = plt.figure(figsize=(8,5))
    ax = sns.scatterplot(x='total_bill', y='tip', data=tips, hue='size')
    ax.set_title('Размер счета и чаевых')
    ax.set_xlabel('Размер счета')
    ax.set_ylabel('Чаевые')
    st.pyplot(fig)
    plt.savefig('3.png')
    with open("3.png", 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='3.png', mime='image/png' )

button4 = st.sidebar.button('График чаевые/день недели')
if button4:
    fig = plt.figure(figsize=(8,5))
    tips['weekday'] = tips['time_order'].dt.weekday
    ax = sns.scatterplot(x='tip', y='weekday', hue='sex', data=tips )
    ax.set_title('График чаевые/день недели')
    ax.set_xlabel('Чаевые')
    ax.set_ylabel('День недели')
    st.pyplot(fig)
    plt.savefig('4.png')
    with open(fig, 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='4.png', mime='image/png' )

button5 = st.sidebar.button('Сумма всех счетов за каждый день')
if button5:
    fig = plt.figure(figsize=(8,10))
    ax = sns.boxplot(data=tips, x='total_bill', y='time_order', hue='time' )
    ax.set_title('Сумма всех счетов за каждый день')
    ax.set_xlabel('Размер счета')
    ax.set_ylabel('Дата')
    st.pyplot(fig)
    plt.savefig('5.png')
    with open("5.png", 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='5.png', mime='image/png' )

button6 = st.sidebar.button('Графики чаевых обед/ланч')
if button6:
    ax = sns.displot(data=tips, x="tip", kind='hist', col='time')
    ax.set_titles('График чаевых обед/ланч')
    ax.set_xlabels('Размер чаевых')
    ax.set_ylabels('Количество')
    st.pyplot(ax)
    plt.savefig('6.png')
    with open("6.png", 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='6.png', mime='image/png' )

button7 = st.sidebar.button('График размера счета и чаевых(доп)')
if button7:
    ax = sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker', col='sex', kind='scatter')
    ax.set_xlabels('Размер счета')
    ax.set_ylabels('Размер чаевых')
    st.pyplot(ax)
    plt.savefig('7.png')
    with open("7.png", 'rb') as file:
        dw = st.sidebar.download_button(label='Скачать график', data=file,file_name='7.png', mime='image/png' )