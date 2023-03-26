import streamlit as st
import pandas as pd
import numpy as np

st.title('Tera Fifa Project')

option = st.selectbox(
    'Posição Procurada',
    (
        'Atacante', 
        'Goleiros', 
        'Meiocampista', 
        'Laterais', 
        'Zagueiros'
    )
)

df = pd.read_csv("C:/Users/Germano/Documents/tera-project-fifa/base/base.csv", low_memory=False)

df = df[df['ano']==22]

df['value_diff'] = df['previsto'] - df['value_eur']

# df = df[df['posicao']==option]

st.table(data=df.head(10))
