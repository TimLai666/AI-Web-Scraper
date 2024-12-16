from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_website(website: str) -> str:
    print("正在啟動瀏覽器...")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(website)
        print("成功連線到網站")
        time.sleep(10)
        html: str = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find("body")
    return body.prettify() if body else ""

def clean_body_content(body: str) -> str:
    soup = BeautifulSoup(body, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content: str = soup.get_text(separator="\n")
    cleaned_content = "\n".join(stripped_line for line in cleaned_content.splitlines() if (stripped_line := line.strip()))

    return cleaned_content

def split_dom_content(dom_content: str, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]