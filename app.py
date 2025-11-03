import streamlit as st

def get_tsla_price():
    return "TSLA: $470.21 (+2.99%)"

def get_tesla_news():
    return "Tesla, yeni batarya hattını duyurdu."

def get_analyst_forecasts():
    return "2026 hedef fiyat: $580"

def get_tesla_order_status():
    return "Model Y siparişleri 4-6 hafta içinde teslim ediliyor."

st.title("Tesla Finansal Agent")
question = st.text_input("Tesla hakkında ne öğrenmek istersin?")

if question:
    if "fiyat" in question:
        st.write(get_tsla_price())
    elif "haber" in question:
        st.write(get_tesla_news())
    elif "analist" in question:
        st.write(get_analyst_forecasts())
    elif "sipariş" in question:
        st.write(get_tesla_order_status())
    else:
        st.write("Bu konuda henüz bilgim yok.")
