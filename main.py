import streamlit as st
import os

st.title("AI Web Scraper")
url = st.text_input("輸入網址")

if st.button("開始爬取"):
    st.write("正在爬取網頁資料...")
