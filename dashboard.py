import streamlit as st
from generatepassword import gerar_senha
from mostrador_senha import *

if "list" not in st.session_state:
    st.session_state.list = []

def save_password(senha):
    new_item = {"icon": "🔒", "description": "Password", "text": f"{senha}"}
    st.session_state.list.append(new_item)

def dashboard():
    st.header('Dashboard')
    tamanho = st.number_input('Tamanho da senha:', min_value=4, step=1, value=12)

    if st.button('Gerar senha'):
        senha = gerar_senha(tamanho)
        st.session_state.generated_password = senha
        st.rerun()
        colum1, colum2 = st.columns([8, 2])
        with colum1:
            st.success(f'Senha gerada: {senha}')
        with colum2:
            if st.button('Salvar senha', key=senha):
                save_password(senha)
    if "generated_password" in st.session_state:
        senha = st.session_state.generated_password
        col1, col2 = st.columns([8, 2])
        with col1:
            st.success(f"Senha gerada: {senha}")
        with col2:
            if st.button("Salvar senha", key=f"save_{senha}"):
                save_password(senha)

def main():
    dashboard()
    st.subheader('Itens Salvos')

    for idx, item in enumerate(st.session_state.list):
        render_list_item(item["icon"], item["description"], item["text"], idx)


if __name__ == '__main__':
    main()
