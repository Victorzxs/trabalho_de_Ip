import streamlit as st
import random
st.title("Adivinhe o número\n")
opcoes = (["facil", "médio", "dificil"])
numeros = []
escolha = st.selectbox("escolha uma dificuldade :" , opcoes)
if escolha == "facil":
    numero = random.randint(1,3)
    st.text("O número está entre 1 e 3\n")
    for i in range(1,4):
       numeros.append(i)
elif escolha == "médio":
    numero = random.randint(1,5)
    st.text("O número está entre 1 e 5\n")
    for i in range(1,6):
       numeros.append(i)
else:
    numero = random.randint(1,10)
    st.text("O número está entre 1 e 10\n")
    for i in range(1,11):
       numeros.append(i)
jogador = st.selectbox("Qual o número ?", numeros)
if st.button("resultado"):
    if jogador == numero:
        st.text("Parabéns, você ganhou !!\n")
    else:
        st.text("Número errado\n")