from bs4 import BeautifulSoup
import requests

#url = 'https://www.bloomingdales.com/shop/makeup-perfume-beauty/luxury-perfume?id=1005889&cm_sp=NAVIGATION-_-TOP_NAV-_-1005889-Fragrance-Perfume'
url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541&cm_sp=NAVIGATION-_-TOP_NAV-_-1001541-Home-Decor-Bowls,-Trays-%26-Vases'

categorylist = ["https://www.bloomingdales.com/shop/jewelry-accessories/earrings?id=3628","https://www.bloomingdales.com/shop/jewelry-accessories/reading-glasses?id=1006684","https://www.bloomingdales.com/shop/home/home-accents-accessories?id=1001543","https://www.bloomingdales.com/shop/home/modern-contemporary-mirrors-wall-art?id=1001546","https://www.bloomingdales.com/shop/home/bakeware?id=1000235","https://www.bloomingdales.com/shop/jewelry-accessories/womens-fashion-necklaces?id=3629","https://www.bloomingdales.com/shop/womens-designer-shoes/all-fashion-shoes?id=17411","https://www.bloomingdales.com/shop/home/modern-contemporary-designer-dining-chairs?id=1005620","https://www.bloomingdales.com/shop/kids/baby-toys-plush?id=1000307","https://www.bloomingdales.com/shop/handbags/womens-handbags-purses?id=17316","https://www.bloomingdales.com/shop/home/glassware-stemware-drinkware?id=1000232","https://www.bloomingdales.com/shop/womens-apparel/formal-dresses-evening-gowns?id=1005210","https://www.bloomingdales.com/shop/kids/designer-baby-strollers-car-seats?id=1006106","https://www.bloomingdales.com/shop/gifts/best-luxury-baby-shower-gifts?id=19459","https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541","https://www.bloomingdales.com/shop/home/luxury-lighting?id=1001009","https://www.bloomingdales.com/shop/home/designer-rugs?id=1001971","https://www.bloomingdales.com/shop/home/serveware?id=1000234","https://www.bloomingdales.com/shop/gifts/best-gifts-under-25?id=1020259","https://www.bloomingdales.com/shop/gifts/best-gifts-under-50?id=1003526","https://www.bloomingdales.com/shop/gifts/best-gifts-under-100?id=1005374"]

for url in categorylist:
	f = open("item_urls.txt", "a")
	f.write('\n\n' + 'Category URL: ' url + '\n')

	#url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}
	response = requests.get(url,headers=headers)
	content = BeautifulSoup(response.content,"html.parser")

	#print(response.status_code) #helpful when ensuring that connection to webpage successful

	#identify chunk of code that contains page number
	select = content.find('select',attrs={"class":"sort-dropdown-values","id":"sort-pagination-select-top"})
	#pull out the last page number
	lastoption = select('option')[-1] #determine the <> that contains total number of pages
	num_of_pages = int(lastoption['value']) #convert from string to integer
	num_of_pages = num_of_pages + 1 #for whatever reason, missing last page count so increment by 1
	#print('num of pages: {}'.format(lastoption['value']))
	print('num of pages var: {}'.format(num_of_pages))


	for eachpage in range(11,13): # to speed up, only it through page 2 and 3
	#for eachpage in range(num_of_pages): # to speed up, only it through 3 pages, range goes from 0 to n-1
	#for eachpage in num_of_pages:
		num_of_pages = str(eachpage+1)  #add 1 so that it from 1 to n and not 0 to n-1 in the url
		url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/' + num_of_pages + '?id=1001541'
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}
		response = requests.get(url,headers=headers)
		page_content = BeautifulSoup(response.content,"html.parser") #pull the entire webpage
		f = open("item_urls.txt", "a")
		f.write('Page '+ str(eachpage) + '\n')

		for item in page_content.findAll('a',attrs={"class":"productDescLink"},href=True): #loop over each thumbnail
			f = open("item_urls.txt", "a")
			f.write('https://www.bloomingdales.com' + item['href'] + '\n') #insert url into file

		

	# Code to iterate over multiple pages
	# First must extract number of pages
	# Then change the page index to scrape each
	##https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/2?id=1001541
	#https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/1?id=1001541