import streamlit as st
import requests

def connect():
    API_URL = "http://127.0.0.1:8000/password/"

    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Connected")
        return response
    else:
        print("Failed to connect")
        return None