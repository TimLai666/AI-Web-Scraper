from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_website(website):
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
        html = driver.page_source
        return html
    finally:
        driver.quit()
