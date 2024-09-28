import streamlit as st
import sqlite3
from fuzzywuzzy import fuzz
import unidecode
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# Função para remover stopwords, acentos e normalizar texto
def preprocessar_texto(texto):
    texto = texto.lower().strip()  # Converte para minúsculas e remove espaços
    texto = unidecode.unidecode(texto)  # Remove acentos
    stop_words = set(stopwords.words('portuguese'))  # Lista de stopwords em português
    palavras = texto.split()
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words]  # Remove stopwords
    return ' '.join(palavras_filtradas)  # Reconstrói a string

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('diagnosticos.db')

# Função para buscar causas e testes com base no problema
def buscar_diagnostico(problema):
    conn = conectar_banco()
    cursor = conn.cursor()

    # Tenta encontrar correspondências exatas primeiro
    cursor.execute('SELECT possiveis_causas, teste FROM diagnosticos WHERE problema = ?', (problema.strip(),))
    resultados_exatos = cursor.fetchall()

    # Log para depuração
    print(f"Buscando problema exato: {problema.strip()}")
    print(f"Resultados Exatos: {resultados_exatos}")

    # Se encontrou correspondências exatas, retorna imediatamente
    if resultados_exatos:
        conn.close()
        return resultados_exatos, True  # Indica que houve correspondência exata
    
    # Se não encontrar correspondência exata, faz a busca fuzzy  
    cursor.execute('SELECT problema, possiveis_causas, teste FROM diagnosticos')
    diagnosticos = cursor.fetchall()
    
    resultados_fuzzy = []
    problema_preprocessado = preprocessar_texto(problema)

    for diag in diagnosticos:
        problema_bd = preprocessar_texto(diag[0])
        
        # Log para depuração
        print(f"Comparando: {problema_preprocessado} com {problema_bd}")

        # Comparação fuzzy entre o input do usuário e o problema no banco de dados
        similaridade_problema = fuzz.token_sort_ratio(problema_preprocessado, problema_bd)

        # Se a similaridade for maior que 80%, considere como match
        if similaridade_problema > 80:
            resultados_fuzzy.append((diag[1], diag[2]))  # Adiciona possiveis_causas e teste
    
    conn.close()
    return resultados_fuzzy, False  # Indica que não houve correspondência exata

# Interface do Streamlit
st.set_page_config('Diagnóstico Automático de Falhas em Ar Condicionado', page_icon=':material/home_repair_service:')

st.title('Diagnóstico de Defeitos em Ar Condicionado :male-mechanic:')
problema = st.text_input('Descreva o problema do ar condicionado')

if problema:
    resultados, correspondencia_exata = buscar_diagnostico(problema)
    
    if resultados:
        if correspondencia_exata:
            st.subheader('Possíveis Causas e Testes (Correspondência Exata):')
        else:
            st.subheader('Possíveis Causas e Testes (Correspondências Aproximadas):')
        
        for causa, teste in resultados:
            st.write(f'**Causa**: {causa}')
            st.write(f'**Teste**: {teste}')
            st.write('---')
    else:
        st.warning('Problema não encontrado no banco de dados')


