from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import os
import time

def scrape_mars():

    executable_path = {"executable_path": "C:\\Users\\shane\\Downloads\\Resources\\chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/"

    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    nasa_title = soup.find('a', target="_self").text
    nasa_teaser = soup.find('div', class_='article_teaser_body').text
    
    executable_path = {"executable_path": "C:\\Users\\shane\\Downloads\\Resources\\chromedriver.exe"}
    browser = Browser("chrome", **executable_path)

    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

    browser.visit(url)
    html = browser.html
    img_soup = bs(html, 'html.parser')

    urlb = soup.find_all("img")

    urlb = img_soup.find('img', class_='headerimage')['src']

    html = browser.html
    img_soup = bs(html, 'html.parser')


    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{urlb}"
    
    url = "https://space-facts.com/mars/"

    fact_tables = pd.read_html(url)[0].to_html()
    fact_tables
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)
    html = browser.html
    hemi_soup = bs(html, 'html.parser')

    banners_tag = hemi_soup.find_all('h3')
    banners = [x.text for x in banners_tag]

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    hemispheres = []
    for i in range(len(banners)):
        hemisphere = {}
        
        browser.visit(url)
        browser.find_by_css('h3')[i].click()
        
        hemisphere[banners[i]] = browser.find_by_text('Sample')['href']
        
        hemispheres.append(hemisphere)
        
        browser.back()

    mars_data = {
        "nasa_title": nasa_title,
        "nasa_teaser": nasa_teaser,
        "featured_image_url": featured_image_url,
        "fact_tables": fact_tables,
        "hemispheres": hemispheres
    }