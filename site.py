#importando a bliblioteca

import streamlit as st 
import time

#titulo com o nome do sistema

titulo = st.title("Sistema de Análise de Crédito")

#criando um formularío para o cliente preencher 

nome = st.text_input("Nome") # inserir um texto
idade = st.number_input("Idade") # Inserir a idade
renda = st.number_input("Renda Mensal") # Inserir a renda mensal
score = st.number_input("Score") # Inserir o score


#Criando um botão para o cliente clicar e validar as informações
if st.button("Validar"): # Criando um botão para validar as informações
    with st.spinner("Validando as informações..."): # Criando um spinner para mostrar que o sistema está validando as informações
        time.sleep(2) # Criando um tempo de espera para simular a validação das informações
    if idade < 18: # Validando se o cliente é maior que 18 anos
        st.error("Negado por idade") # Caso seja menor que 18 anos, irá retornar esta mensagem
    elif renda < 1200: # Validando se a renda é menor que 1200
        st.error("Negado por renda") # Caso seja menor que 1200, irá retornar esta mensagem
    elif score < 400: # Validando se o score é menor que 400
        st.error("Infelizmente você foi reprovado") # Caso seja menor que 400, irá retornar esta mensagem
    else:
        st.success("Parabéns, você foi APROVADO!") # Caso seja maior que 400, irá retornar esta mensagem