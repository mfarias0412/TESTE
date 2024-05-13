import streamlit as st

# Caminho para a imagem
caminho_imagem = 'C:\\Users\\MFARIAS\OneDrive - Firjan\\Imagens\\fla.jpg'

# Carrega a imagem
imagem = st.image(caminho_imagem, caption='Sua Imagem', use_column_width=True)


