# Find the price of a graphics card on Newegg site

from bs4 import BeautifulSoup
import requests

# send an http request to this url, and return the content of the page
url = 'https://www.newegg.ca/asus-geforce-rtx-4070-ti-tuf-rtx4070ti-o12g-gaming/p/N82E16814126606'
my_result = requests.get(url)

# store the content of the page in my_result.text
# print(my_result.text)

# use BeautifulSoup
my_document = BeautifulSoup(my_result.text, 'html.parser')
# print the html text, with tags and all
# print(my_document.prettify())

# find the price in the html page
# 1. find '$'
prices = my_document.find_all(text='$')
print(prices)

# find the parent of '$'
parent = prices[0].parent
print(parent)

# now search for the parent tag where we see the price
parent_tag = parent.find('strong')
print(parent_tag)
# and to only get the actual number representing the price:
print(parent_tag.string)
