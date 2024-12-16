import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content
)

st.title("AI Web Scraper")
url = st.text_input("輸入網址")

if st.button("開始爬取"):
    st.write("正在爬取網頁資料...")
    html: str = scrape_website(url)
    body: str = extract_body_content(html)
    cleaned_content: str = clean_body_content(body)
    st.session_state.dom_content = split_dom_content(cleaned_content)

    with st.expander("爬取結果", expanded=True):
        st.text_area(f"{url} 的爬取結果：", cleaned_content, height=300)
