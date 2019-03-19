

from bs4 import BeautifulSoup
import requests

url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541&cm_sp=NAVIGATION-_-TOP_NAV-_-1001541-Home-Decor-Bowls,-Trays-%26-Vases'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}
response = requests.get(url,headers=headers)
content = BeautifulSoup(response.content,"html.parser")

bowlArr = []
print(response.status_code)
for item in content.findAll('a',attrs={"class":"productDescLink"},href=True):
	#f = open("demofile.txt", "a")
	#f.write("Now the file has one more line!")
	#f.write(item.text.encode('utf-8'))
	print("Found the URL:", item['href'])
# Next write the url to a file that can be easily parsed, iterate over each page.
# Notice the category id in each URL is identical for each category

