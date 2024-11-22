import streamlit as st
import requests
from supabse import create_client,client

SUPABSE_URL="https://nirofruznluznvcrenzq.supabase.co"
SUPABASE_KEY ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5pcm9mcnV6bmx1em52Y3JlbnpxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYzNTk5NzIsImV4cCI6MjA0MTkzNTk3Mn0.8DxdMyiyv-J60FUraexHkiA_4YWKdzTvYBconoHmoOE"
supabse: Client = create_client(SUPABSE_URL,SUPABASE_KEY)


def get_exchange_rate(base_currency ="USD",target_currency ="EUR"):
    url =f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response= requests.get(url)
    if(response.status_code==200):
        return response.json()
    else:
        return{"error":"No se puedo conectar con el api"}    

def save_to_supase(data):
    response = supabse.table("exchange_rates").insert(data).execute()
    return response
