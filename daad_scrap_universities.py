import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


 
options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

unique_links = set()
with open("daad_all_universities_links.txt", "w") as fd:
    fd.write("Computer Science Universities\n")

def fetch_links(url):
    driver.get(url)
    # Wait for the accept button to be clickable
    accept_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'snoop-button.qa-cookie-consent-accept-all.snoop-button--primary'))
    )

    # Click the accept button
    accept_button.click()    
    time.sleep(10)

    while True:
        try:
            # Once content is loaded, get the page source
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Extract links using BeautifulSoup as before
            time.sleep(5)
            links = soup.find_all("a")
            for link in links:
                if "#" in link.get("href") or "https" in link.get("href"):
                    continue
                unique_links.add(link.get("href"))

            print("Clicking Next BTN ...")
            next_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div/div[1]/div[2]/a[2]')
            next_btn.click()

        except Exception as ex:
            print(ex)  
            break

url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=information%20communication%20systems&degree%5B%5D=2&lang%5B%5D=2&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=7&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&fee=1&bgn%5B%5D=1&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=3&dur=&subjects%5B%5D=&limit=100&offset=&display=list"
fetch_links(url)


print(f"Total Universities in Computer Science: {len(unique_links)}")
# Writing to a file
with open("daad_all_universities_links.txt", "a") as fd:
    for link in unique_links:    
        fd.write(f"{link}\n")