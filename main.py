from bs4 import BeautifulSoup
import requests
import lxml
import time

docs_url = ("https://docs.google.com/forms/d/e/1FAIpQLSf0oEeysPbsheWFQB4NI"
            "8gq5_BG9JnOdeWH2dbrH0si2CEHxg/viewform?usp=sf_link")
zillow_url = ("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22paginati"
              "on%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.93870009375%2C%2"
              "2east%22%3A-122.092752828125%2C%22south%22%3A37.650084580190374%2C%22nort"
              "h%22%3A37.96581752539461%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%2"
              "2%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%"
              "3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22"
              "%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22val"
              "ue%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%2"
              "2value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%"
              "3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                  "/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
}
response = requests.get(zillow_url, headers=header)
web_html = response.content
soup = BeautifulSoup(web_html, "lxml")

time.sleep(5)
x = soup.select('h1')
print(x)
# all_data = soup.select("div div article div div a[href]")
# links = []
# for data in all_data:
#     link = data.get("href")
#     links.append(f"https://www.zillow.com{link}")
# n = 0
# for data in links:
#     if n % 2 == 0 or n == 0:
#         links.remove(data)
#
# all_prices = soup.select("div div article div div div div span[data-test=property-card-price]")
# prices = []
# for data in all_prices:
#     whole_price = data.text
#     prices.append(whole_price.split("+")[0])
#
# all_add = soup.select("div div article div div a address")
# addresses = []
# for add in all_add:
#     addresses.append(add.text)
#
#
# print(addresses)
# print(prices)
# print(links)
# print(len(addresses))
# print(len(prices))
# print(len(links))




