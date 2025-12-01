import pandas as pd
import plotly.express as px
import streamlit as st
from time import sleep

st.set_page_config(page_title = "Vacinações",layout="wide")

st.title("DASHBOARD VACINAÇÃO")

df = pd.read_csv('vacinacao_corrigido.csv')

fig1 = px.line(df, x = 'date', y = 'total_vaccinations', color = 'location',
               title = 'Total de vacinações por país')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Total de vacinações', title_font_size = 30)
fig1.show()

st.plotly_chart(fig1, use_container_width = True)

df_brasil_usa_india = df.query('location == "BRAZIL" or location == "UNITED STATES" or location == "INDIA"')

i = int(input("Digite quantos termos: "))
while i != 0:
    a, b = 0, 1
    c = 0
    while c < i:
        if a != 0:
            print(str(c+1)+": "+str(b)+"--------"+str(b/a))
            sleep(.5) #pequena pausa para mostrar a próxima linha
            a, b = b, a+b
            c += 1
        else:
            print(str(c+1)+": "+str(b))
            sleep(.5)
            a, b = b, a+b
            c += 1
    i = int(input("Digite quantos termos: "))


fig2 = px.pie(df_brasil_usa_india, values = 'total_vaccinations', names = 'location', title = 'Total de vacinados no Brasil, USA e Índia')
fig2.show()

st.plotly_chart(fig2, use_container_width = True)

