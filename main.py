import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Vacinações",layout="wide")

st.title("DASHBOARD VACINAÇÃO")

df = pd.read_csv('vacinacao_corrigido.csv')

fig1 = px.line(df, x = 'date', y = 'total_vaccinations', color = 'location',
               title = 'Total de vacinações por país')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Total de vacinações', title_font_size = 30)
fig1.show()

st.plotly_chart(fig1, use_container_width = True)

df_brasil_usa_india = df.query('location == "BRAZIL" or location == "UNITED STATES" or location == "INDIA"')


