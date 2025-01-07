import streamlit as st
import server
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
    new_item = {"icon": f"{emoji}", "description": f"{descricao}", "text": f"{senha}"}
    st.session_state.list.append(new_item)

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
                        st.success("Senha salva com sucesso!")
                    else:
                        st.error("A descrição não pode estar vazia!")

def main():
    status_server = server.connect()
    if status_server:
        dashboard()
        st.subheader('Itens Salvos')

        for idx, item in enumerate(st.session_state.list):
            render_list_item(item["icon"], item["description"], item["text"], idx)
    else:
        st.subheader('Server Error')

if __name__ == '__main__':
    main()
