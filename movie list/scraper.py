import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.keys import Keys
from lxml import etree
import requests
import urllib


siteLink = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

driver.get(siteLink)
soup = BeautifulSoup(driver.page_source, "html.parser")
dom = etree.HTML(str(soup))

movieCoverLink = []
movieTitle = []
movieYearLink = []

for i in range(1, 251):
    title = dom.xpath("/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[%s]/div[2]/div/div/div[1]/a/h3" %i)[0].text
    moviePoster = dom.xpath("/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[%s]/div[1]/div/div[2]/img/@src" %i)[0]
    movieYear =  dom.xpath("/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[%s]/div[2]/div/div/div[2]/span[1]" %i)[0].text
    movieTitle.append(title)
    movieCoverLink.append(moviePoster)
    movieYearLink.append(movieYear)

print(movieTitle)
print(movieCoverLink)
print(movieYearLink)


time.sleep(2000)
