#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# In[12]:


def scrape_wikipedia_page(url):
    """Scrapes a Wikipedia page given its URL."""
    response = req.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return {
        "title": get_article_titles(soup),
        "text_by_heading": get_article_text(soup),
        "wikipedia_links": extract_wikipedia_links(soup)
    }


# In[4]:


def get_article_titles(soup):
#     """Finds all the article titles in the HTML page."""
     return [title.text.strip() for title in soup.find_all('h2')]
    


# In[5]:


def get_article_text(soup):
#     """Extracts article text for each paragraph with their respective headings."""
     content = {}
     main_content = soup.find('div', {'id': 'bodyContent'})

     if main_content:
         for section in main_content.find_all(['h2', 'h3']):
             heading = section.text.strip()
             paragraphs = []
             for sibling in section.find_next_siblings():
                 if sibling.name in ['h2', 'h3']:
                     break
                 if sibling.name == 'p':
                     paragraphs.append(sibling.text.strip())
             content[heading] = ' '.join(paragraphs)
     return content


# In[6]:


def extract_wikipedia_links(soup):
     """Collects all links that redirect to another Wikipedia page."""
     links = set()
     base_url = "https://en.wikipedia.org"
     for a_tag in soup.find_all('a', href=True):
         href = a_tag['href']
         if href.startswith('/wiki/') and ':' not in href:  # Exclude special links like files
             full_url = urljoin(base_url, href)
             links.add(full_url)
     return links


# In[13]:


# Test the function
if __name__ == "__main__":
     test_url = "https://en.wikipedia.org/wiki/Mountain_pigeon"
     scraped_data = scrape_wikipedia_page(test_url)

     # Print results
     print("Title:", scraped_data["title"])
     print("\nText by Heading:")
     for heading, text in scraped_data["text_by_heading"].items():
         print(f"\n{heading}:\n{text[:200]}...\n")

     print("\nWikipedia Links:")
     print(list(scraped_data["wikipedia_links"])[:10])  # Display first 10 links


# In[ ]:


"""This script is a simple yet effective way to scrape and organize information from Wikipedia pages.
    It demonstrates the use of web scraping techniques in Python,
    handling HTTP requests, and parsing HTML content."""
"""This code is a Python script that scrapes content from a Wikipedia page using the requests library to fetch the HTML content and BeautifulSoup to parse it.
The script extracts article titles, text organized by headings, and links to other Wikipedia pages.
"""
