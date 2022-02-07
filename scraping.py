#!/usr/bin/env python
# coding: utf-8

# In[30]:

# import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# In[6]:

executable_path ={'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False) 

# In[8]:

# visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page
browser.is_element_present_by_css('div.list_text',wait_time=1)

# In[12]:

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# In[21]:

slide_elem.find('div', class_='content_title')


# In[22]:

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_= 'content_title').get_text()
news_title

# In[23]:

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_= 'article_teaser_body').get_text()
news_title

# In[24]:

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# In[25]:

#find and click the full image botton
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# In[27]:

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# In[28]:

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# In[29]:

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# In[31]:

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# In[32]:

df.to_html()

# In[33]:

browser.quit()