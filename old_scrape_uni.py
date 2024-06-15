import requests
from bs4 import BeautifulSoup
import time
import random
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def check_website(url):
    afile = open("user-agents.txt")
    headers = random_line(afile).rstrip()  # Random header for bypassing security checks on the website
    print(f"Header is: {headers}")
    try:
        response = requests.get(url, headers={'User-Agent': headers}, timeout=100)
        # print(f"Below is response error if exists ---  0000  ----")
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the desired text in the parsed HTML (case-insensitive)
        # print(soup.get_text().lower())
        links = soup.find_all("a") # Find all elements with the tag <a>
        for link in links:
            print("Link:", link.get("href"), "Text:", link.string)
            # print(link)

    except Exception as e:
        print(f"Error: {e}")
    return False


def random_line(afile):
    lines = afile.readlines()
    return random.choice(lines) 


url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=Computer%20Science&degree%5B%5D=2&lang%5B%5D=2&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&fee=&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=3&dur=&subjects%5B%5D=&limit=100&offset=&display=list"
check_website(url)




