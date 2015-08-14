import requests
from urllib.parse import urljoin
import bs4

home_url = "http://news.stanford.edu/news/"
home_page = requests.get(home_url).text
home_soup = bs4.BeautifulSoup(home_page)
topic_links = home_soup.select('.topiclist a')
print ("printing topic_links.../n")
#print (topic_links)
print("There are {} topic links in total" .format(len(topic_links)))
for links in topic_links:
	if links['href'].find('/tags')>-1:
		print("Tagged topic:", links.text, "at URL:", links['href'])
		tag_url = urljoin(home_url, links['href'])
		tpage = requests.get(tag_url).text
		tsoup = bs4.BeautifulSoup(tpage)
		heads = tsoup.select("#main-content .postcard-text")
		#print("Printing heads......")
		#print (heads)
		h = heads[0]
		#print ("Printing HEAD[0]..........................")
		#print (heads[0])
		head = h.find('h3').text
		print("Latest headline: {}" .format(head))
		print("")