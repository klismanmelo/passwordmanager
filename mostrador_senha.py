import streamlit as st
import pyperclip as pp
from server import delete_password


def render_list_item(icon, description, text, index):
    col1, col2, col3, col4 = st.columns([1, 2, 4, 3])  # Layout com colunas
    with col1:
        st.markdown(f"<span style='font-size: 20px;'>{icon}</span>", unsafe_allow_html=True)
    with col2:
        st.write(description)
    with col3:
        masked_text = "*" * len(text)  # Texto mascarado
        key_show = f"show_{index}"
        if st.session_state.get(key_show, False):
            st.write(text)  # Mostra o texto original
        else:
            st.write(masked_text)
    with col4:
        copy_col, toggle_col, delete_col = st.columns([1, 1, 1])
        with copy_col:
            if st.button("🔍", key=f"copy_{index}"):
                pp.copy(text)
        with toggle_col:
            if st.button("👁️", key=f"toggle_{index}"):
                st.session_state[f"show_{index}"] = not st.session_state.get(f"show_{index}", False)
        with delete_col:
            if st.button("❌", key=f"delete_{index}"):
                delete_password(index)
                st.rerun()

