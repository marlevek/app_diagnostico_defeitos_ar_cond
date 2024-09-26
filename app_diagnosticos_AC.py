import streamlit as st
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('diagnosticos.db')

# Função para buscar causas e testes com base no problema
def buscar_diagnostico(problema):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT possiveis_causas, teste FROM diagnosticos WHERE problema LIKE ?', ('%' + problema + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# Interface do Streamlit
st.set_page_config('Diagnóstico Automático de Falhas em Ar Condicionado', page_icon=':material/search:')

st.title('Diagnóstico de Defeitos em Ar Condicionado :male-scientist:')
problema = st.text_input('Descreva o problea do ar condicionado')

if problema:
    resultados = buscar_diagnostico(problema)
    
    if resultados:
        st.subheader('Possíveis Causas e Testes:')
        for causa, teste in resultados:
            st.write(f'**Causa**: {causa}')
            st.write(f'**Teste**: {teste}')
            st.write('---')
    else:
        st.warning('Problema não encontrado no banco de dados')