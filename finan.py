import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Функция приложения
def show_predict_page():
    st.markdown('''<a href="http://kaizen-consult.ru/"><img src='https://www.kaizen.com/images/kaizen_logo.png' style="width: 50%; margin-left: 25%; margin-right: 25%; text-align: center;"></a><p>''', unsafe_allow_html=True)
    val = st.text_input("Единица измерения", value="Тыс. руб., Млн. руб. или что-либо другое")
    st.title("Анализ ликвидности")
    stroka_1250 = st.number_input(f"Денежные средства и денежные эквиваленты (строка 1250), {val} на конец пероида:", value=0)
    stroka_1240 = st.number_input(f"Финансовые вложения (за исключением денежных эквивалентов) (строка 1240), {val} на конец пероида:", value=0)

# Вызываем приложение

show_predict_page()
