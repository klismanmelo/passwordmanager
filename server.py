import streamlit as st
import requests

def connect():
    API_URL = "http://127.0.0.1:8000/password/"

    response = requests.get(API_URL)
    if response.status_code == 200:
        return response
    else:
        print("Failed to connect")
        return None

def list_passwords():
    API_URL = "http://127.0.0.1:8000/password/"
    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to connect")
            return None
    except:
        print("Failed to connect")

def delete_password(id_password):
    API_URL = "http://127.0.0.1:8000/password/"
    try:
        # Fazendo a requisição DELETE com o ID
        response = requests.delete(f"{API_URL}{id_password}/")
        if response.status_code == 204:
            print("Successfully deleted")
        else:
            print("Failed to delete")
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")