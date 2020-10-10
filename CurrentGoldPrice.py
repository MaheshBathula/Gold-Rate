from bs4 import BeautifulSoup as BS
import requests

#Method to get the price of gold
def getPrice(url):
    data = requests.get(url) #get the request from URL
    soup = BS(data.text, 'html.parser') #Converting the text
    ans = soup.find("div", id="current-price").text #finding metha info for the current price
    return ans

# URL of the gold price
url = "https://www.goodreturns.in/gold-rates/"
ans = getPrice(url)
print("Current Gold Price in India is" + ans)