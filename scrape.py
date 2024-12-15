import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("正在啟動瀏覽器...")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    