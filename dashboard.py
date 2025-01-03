import streamlit as st
from generatepassword import gerar_senha
from mostrador_senha import *

def save_password(senha):
    pass
def dashboard():
    st.header('Dashboard')
    tamanho = st.number_input('Tamanho da senha:', min_value=4, step=1, value=12)

    if st.button('Gerar senha'):
        senha = gerar_senha(tamanho)
        colum1, colum2 = st.columns([8, 2])
        with colum1:
            st.success(f'Senha gerada: {senha}')
        with colum2:
            if st.button('Salvar senha'):
                save_password(senha)

def main():
    items = [
        {"icon": "🔑", "description": "API Key", "text": "12345-ABCDE"},
        {"icon": "🔒", "description": "Password", "text": "mysecretpassword"},
        {"icon": "📧", "description": "Email", "text": "example@mail.com"},
    ]
    dashboard()
    for item in items:
        render_list_item(item["icon"], item["description"], item["text"])


if __name__ == '__main__':
    main()
