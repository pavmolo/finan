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
    stroka_1520 = st.number_input(f"Кредиторская задолженность (строка 1520), {val} на конец пероида:", value=0)
    
    stroka_1230 = st.number_input(f"Дебиторская задолженность (строка 1230), {val} на конец пероида:", value=0)
    stroka_1260 = st.number_input(f"Прочие оборотные активы (строка 1260), {val} на конец пероида:", value=0)
    stroka_1510 = st.number_input(f"Заемные средства (строка 1510), {val} на конец пероида:", value=0)
    stroka_1550 = st.number_input(f"Прочие обязательства (строка 1550), {val} на конец пероида:", value=0)
    
    stroka_1210 = st.number_input(f"Запасы (строка 1210), {val} на конец пероида:", value=0)
    stroka_1170 = st.number_input(f"Финансовые вложения (строка 1170), {val} на конец пероида:", value=0)
    stroka_1400 = st.number_input(f"Долгосрочные обязательства (строка 1400), {val} на конец пероида:", value=0)
    
    stroka_1100 = st.number_input(f"Внеоборотные активы (строка 1100), {val} на конец пероида:", value=0)
    stroka_1300 = st.number_input(f"Капитал и резервы (строка 1300), {val} на конец пероида:", value=0)
    stroka_1530 = st.number_input(f"Доходы будущих периодов (строка 1530), {val} на конец пероида:", value=0)
    stroka_1540 = st.number_input(f"Оценочные обязательства (строка 1540), {val} на конец пероида:", value=0)
    
    st.header('Группы ликвидности')
    st.subheader(f'Самые ликвидные (А1) = {stroka_1250 + stroka_1240} {val}')
    
# Вызываем приложение

show_predict_page()
