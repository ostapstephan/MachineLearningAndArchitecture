from bs4 import BeautifulSoup
import requests

#url = 'https://www.bloomingdales.com/shop/makeup-perfume-beauty/luxury-perfume?id=1005889&cm_sp=NAVIGATION-_-TOP_NAV-_-1005889-Fragrance-Perfume'
url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541&cm_sp=NAVIGATION-_-TOP_NAV-_-1001541-Home-Decor-Bowls,-Trays-%26-Vases'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}
response = requests.get(url,headers=headers)
content = BeautifulSoup(response.content,"html.parser")

bowlArr = []
print(response.status_code)

# Determine how many pages exist under this category. For unknown reasons, the number of pages returned is one less than the actual number of pages
for select in content.findAll('select',attrs={"class":"sort-dropdown-values","id":"sort-pagination-select-top"}):
	for option in select.findAll('option'):
		print('page values: {}'.format(option['value']))

# Determine how many pages exist under this category. For unknown reasons, the number of pages returned is one less than the actual number of pages
# Also note that the page number field is repeated twice on each page, so this code iterates twice, both identical
for select in content.findAll('select',attrs={"class":"sort-dropdown-values","id":"sort-pagination-select-top"}):
	lastoption = select('option')[-1]
	num_of_pages = int(lastoption['value']) #convert from string to integer
	num_of_pages = num_of_pages + 1 #for whatever reason, it is missing last page count
	#print('num of pages: {}'.format(lastoption['value']))
	print('num of pages var: {}'.format(num_of_pages))


for eachpage in range(2,4): # to speed up, only it through page 2 and 3
#for eachpage in range(num_of_pages): # to speed up, only it through 3 pages, range goes from 0 to n-1
#for eachpage in num_of_pages:
	url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/' + eachpage+1 + '?id=1001541' #add 1 so that it from 1 to n and not 0 to n-1 in the url
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}
	response = requests.get(url,headers=headers)
	page_content = BeautifulSoup(response.content,"html.parser")
	f = open("demofile.txt", "a")
	f.write('Page\n')
	f.write(eachpage)

	for item in page_content.findAll('a',attrs={"class":"productDescLink"},href=True):
		f = open("demofile.txt", "a")
		f.write("Now the file has one more line!")
		f.write(item['href'].text.encode('utf-8'))
		#print("Found the URL:", item['href'])	

	
	





#WORKS  for item in content.findAll('a',attrs={"class":"productDescLink"},href=True):
#f = open("demofile.txt", "a")
#f.write("Now the file has one more line!")
#f.write(item.text.encode('utf-8'))
#WORKS  print("Found the URL:", item['href'])
# Next write the url to a file that can be easily parsed, iterate over each page.
# Notice the category id in each URL is identical for each category

# Code to iterate over multiple pages
# First must extract number of pages
# Then change the page index to scrape each
##https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/2?id=1001541
#https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/1?id=1001541