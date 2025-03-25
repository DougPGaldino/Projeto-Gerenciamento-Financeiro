import streamlit as st
import pandas as pd
import Funcoes

st.title("Gerenciamento de Finanças")

nome = st.text_input("Digite o nome do usuário")
senha = st.text_input("Digite uma senha")

if st.button("Adicionar Usuário"):
    Funcoes.InserirUsuario(nome,senha)
    st.success("Usuário Adicionado!")

