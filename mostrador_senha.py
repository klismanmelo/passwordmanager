import streamlit as st
import pyperclip as pp

# Função para renderizar um item da lista
def render_list_item(icon, description, text):
    col1, col2, col3, col4 = st.columns([1, 2, 4, 2])  # Layout com colunas
    with col1:
        st.markdown(f"<span style='font-size: 20px;'>{icon}</span>", unsafe_allow_html=True)
    with col2:
        st.write(description)
    with col3:
        masked_text = "*" * len(text)  # Texto mascarado
        if st.session_state.get(f"show_{description}", False):
            st.write(text)  # Mostra o texto original
        else:
            st.write(masked_text)  # Mostra o texto mascarado
    with col4:
        copy_col, toggle_col = st.columns([1, 1])
        with copy_col:
            if st.button("📋", key=f"copy_{description}"):
                pp.copy(text)
        with toggle_col:
            if st.button("👁️", key=f"toggle_{description}"):
                st.session_state[f"show_{description}"] = not st.session_state.get(f"show_{description}", False)


# Inicializar o estado se necessário
if "clipboard" not in st.session_state:
    st.session_state.clipboard = ""
