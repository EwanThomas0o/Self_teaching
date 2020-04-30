import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/Essential-Diffuser-Humidifier-Ultrasonic-Aromatherapy/dp/B083LZ7GN4/ref=sr_1_19?dchild=1&keywords=diffuser&qid=1588168192&sr=8-19'  #The URL that we'll be tracking the price of.

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'} #Allows us to get information on the browser, this tells the website what browser we're using on what device. Done as HTTPS requests from different devices are all sent differently 

page = requests.get(URL, headers=headers) #Throws all data from website -> in JSON format

# We then use BeautifulSoup to sift through all the data, and retrieve what we want!

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id="productTitle").get_text()

print(title.strip())

price = soup2.find(id = "priceblock_ourprice").get_text()

corrected_price = float(price.replace('£',''))

print(corrected_price)

if(converted_price < 15):
    send_mail()