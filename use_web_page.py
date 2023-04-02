# Find the price of a graphics card on Newegg site

from bs4 import BeautifulSoup
import requests

# send an http request to this url, and return the content of the page
url = 'https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product'
my_result = requests.get(url)

# store the content of the page in my_result.text
print(my_result.text)
