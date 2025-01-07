import streamlit as st
import server
import requests

from generatepassword import gerar_senha
from mostrador_senha import *


TIPOS_DE_EMOJIS = [
    '🔑', '🔐', '🗝️', '🔒', '👁️‍🗨️', '👀'
]

if "list" not in st.session_state:
    st.session_state.list = []

if "generated_password" not in st.session_state:
    st.session_state.generated_password = None

def save_password(senha, emoji, descricao):
    API_URL = "http://127.0.0.1:8000/password/"

    payload = {
        "emoji": emoji,
        "description": descricao,
        "password": senha
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200 or response.status_code == 201 :
            data = response.json()
            st.success(f"Senha gerada com sucesso!")
        else:
            st.error(f"Erro na API: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")


def dashboard():
    st.header('Dashboard')
    tamanho = st.number_input('Tamanho da senha:', min_value=4, step=1, value=12)

    colum1, colum2, colum3, colum4 = st.columns(4)
    with colum1:
        maiusculas = st.checkbox("MAIÚSCULAS")
    with colum2:
        minusculas = st.checkbox("minusculas")
    with colum3:
        numeros = st.checkbox("Números")
    with colum4:
        especiais = st.checkbox("Especiais")


    if maiusculas or minusculas or numeros or especiais:
        if st.button('Gerar senha'):
            senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais)
            st.session_state.generated_password = senha
            st.rerun()

        if st.session_state.generated_password:
            senha = st.session_state.generated_password
            st.success(f"Senha gerada: {senha}")

            with st.expander("Salvar senha"):
                col1, col2 = st.columns([1, 4])
                with col1:
                    emoji = st.selectbox("Emoji", TIPOS_DE_EMOJIS)
                with col2:
                    descricao = st.text_input("Descrição")

                if st.button("Salvar", key=f"save_{senha}"):
                    if descricao.strip():
                        save_password(senha, emoji, descricao)
                        st.session_state.generated_password = None
                    else:
                        st.error("A descrição não pode estar vazia!")

def main():
    status_server = server.connect()
    if status_server:
        dashboard()
        st.subheader('Itens Salvos')

        passwords_list = server.list_passwords()

        emoji = list['emoji']
        descricao = list['description']
        password = list['password']
        id = list['id_password']

        if isinstance(passwords_list, list):  # Garantir que o retorno seja uma lista
            for idx, item in enumerate(passwords_list):
                emoji = item.get('emoji', '🔒')  # Fallback se 'emoji' não existir
                description = item.get('description', 'Descrição não fornecida')
                password = item.get('password', 'N/A')
                id_password = item.get('id_password', idx)

                # Renderiza cada item da lista
                render_list_item(emoji, description, password, id_password)

        #for idx, item in enumerate(st.session_state.list):
        #    render_list_item(item["icon"], item["description"], item["text"], idx)
    else:
        st.subheader('Server Error')

if __name__ == '__main__':
    main()
