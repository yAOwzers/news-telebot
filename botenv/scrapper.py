from operator import index
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import logging

scrapeUrl = "https://www.channelnewsasia.com/latest-news"
cnaUrl = "https://www.channelnewsasia.com/"

logging.basicConfig(filename="scrapper.log", level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")
                    
# url scrapper for CNA, get top 5 articales
def scrape():
  # create url
  url = scrapeUrl
  # define headers
  headers = { 'User-Agent': 'Generic user agent' }
  # get page
  page = requests.get(url, headers=headers)
  # let's soup the page
  soup = BeautifulSoup(page.text, 'html.parser')


  arr = soup.find_all('h6')

  newsHeadlineArr = []
  newsLinkArr = []

  responseArr = []

  count = 1
  for link in arr:

    newsHeadlineArr.append(link.a.get_text().strip())
    newsLinkArr.append(link.a.get('href'))

    newsHeadline = link.a.get_text().strip()
    newsLink = cnaUrl + link.a.get('href')
    logging.debug("news_headline-{}".format(newsHeadline) + " ,news_link-{}".format(newsLink))

    responseArr.append(str(count) + ". " + newsHeadline + "\n" + newsLink)
    count = count + 1
    if (count > 5):
      break
    

  return responseArr
	
# scrape()
