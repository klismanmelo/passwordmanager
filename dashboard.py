import streamlit as st
from generatepassword import gerar_senha

def dashboard():
    st.header('Dashboard')

    tamanho = st.number_input('Tamanho da senha:', min_value=4, step=1, value=12)

    if st.button('Gerar senha'):
        senha = gerar_senha(tamanho)
        st.success(f'Senha gerada: {senha}')


def main():
    dashboard()


if __name__ == '__main__':
    main()
