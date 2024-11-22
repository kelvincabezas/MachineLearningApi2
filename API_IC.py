import streamlit as st
import requests
from supabase import create_client,Client

SUPABSE_URL="https://nirofruznluznvcrenzq.supabase.co"
SUPABASE_KEY ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5pcm9mcnV6bmx1em52Y3JlbnpxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYzNTk5NzIsImV4cCI6MjA0MTkzNTk3Mn0.8DxdMyiyv-J60FUraexHkiA_4YWKdzTvYBconoHmoOE"
supabase: Client = create_client(SUPABSE_URL,SUPABASE_KEY)

def get_exchange_rate(base_currency ="USD",target_currency ="EUR"):
    url =f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response= requests.get(url)
    if(response.status_code==200):
        return response.json()
    else:
        return{"error":"No se puedo conectar con el api"}    

def save_to_supase(data):
    response = supabase.table("exchange_rates").insert(data).execute()
    return response

st.title("Consulta y registro de tipo de cambio")

#"Selecionar las monedas"
base_currency = st.selectbox("Moneda base",["USD","EUR","PEN"])
target_currency = st.selectbox("Moneda Objetivo",["USD","EUR","PEN"])

#Consultar el tipo de cambio
if st.button("Consultar tipo de cambio"):
    exchange_rate_data = get_exchange_rate(base_currency,target_currency)
    if "error" in exchange_rate_data:
        st.error(exchange_rate_data["error"])
    else:
        rate=exchange_rate_data["rates"][target_currency]
        st.sucess(f"1 {base_currency} = {rate} {target_currency}")

    # Espacio para anotar comentarios
    comment = st.text_area("Escribe un comentario sobre esta consulta :")  

    if st.button("guardar en Supabase"):
        data_to_save={
            "base_currency":base_currency,
            "target_currency":target_currency,
            "exchange_rate":rate,
            "comment":comment
        }

        response = save_to_supase(data_to_save)

        if response.status == 201:
            st.succes("Datos guardados exitosamente en supabase")
        else:
            st.error("Error al guardar los datos en Supabse")    


