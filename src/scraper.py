from bs4 import BeautifulSoup
import requests
import re
import time 
import random
#url = 'https://www.bloomingdales.com/shop/makeup-perfume-beauty/luxury-perfume?id=1005889&cm_sp=NAVIGATION-_-TOP_NAV-_-1005889-Fragrance-Perfume'
#url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541&cm_sp=NAVIGATION-_-TOP_NAV-_-1001541-Home-Decor-Bowls,-Trays-%26-Vases'
#in case we want reading glasses again "https://www.bloomingdales.com/shop/jewelry-accessories/reading-glasses?id=1006684",
# 
UrlFile="data/item_urls.txt"

categorylist = [ "https://www.bloomingdales.com/shop/jewelry-accessories/earrings?id=3628",
        "https://www.bloomingdales.com/shop/jewelry-accessories/reading-glasses?id=1006684", 
        "https://www.bloomingdales.com/shop/home/home-accents-accessories?id=1001542",
        "https://www.bloomingdales.com/shop/home/modern-contemporary-mirrors-wall-art?id=1001546",
        "https://www.bloomingdales.com/shop/home/bakeware?id=1000235",
        "https://www.bloomingdales.com/shop/jewelry-accessories/womens-fashion-necklaces?id=3629",
        "https://www.bloomingdales.com/shop/womens-designer-shoes/all-fashion-shoes?id=17411",
        "https://www.bloomingdales.com/shop/home/modern-contemporary-designer-dining-chairs?id=1005620",
        "https://www.bloomingdales.com/shop/kids/baby-toys-plush?id=1000307",
        "https://www.bloomingdales.com/shop/handbags/womens-handbags-purses?id=17316",
        "https://www.bloomingdales.com/shop/home/glassware-stemware-drinkware?id=1000232",
        "https://www.bloomingdales.com/shop/womens-apparel/formal-dresses-evening-gowns?id=1005210",
        "https://www.bloomingdales.com/shop/kids/designer-baby-strollers-car-seats?id=1006106",
        "https://www.bloomingdales.com/shop/gifts/best-luxury-baby-shower-gifts?id=19459",
        "https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541",
        "https://www.bloomingdales.com/shop/home/luxury-lighting?id=1001009",
        "https://www.bloomingdales.com/shop/home/designer-rugs?id=1001971",
        "https://www.bloomingdales.com/shop/home/serveware?id=1000234",
        "https://www.bloomingdales.com/shop/gifts/best-gifts-under-25?id=1020259",
        "https://www.bloomingdales.com/shop/gifts/best-gifts-under-50?id=1003526",
        "https://www.bloomingdales.com/shop/gifts/best-gifts-under-100?id=1005374"]
prepageIndex = []
CategoryId = []

preIdreg  = re.compile('.+\?id=')                                                                                                                                                                       
postIdReg = re.compile('\?id=.*')   

for i in categorylist:
    mo = preIdreg.search(i)                                                                                                                                                                             
    prepageIndex.append(mo.group()[:-4]) 
    mo = postIdReg.search(i) 
    CategoryId.append(mo.group())


for i in range(len(categorylist)):
    print('\t'+prepageIndex[i]+'\t'+CategoryId[i])


i=0
for url in categorylist:
    f = open(UrlFile, "a")
    f.write('\n\n' + 'Category URL: ' + url + '\n')

    # url = 'https://www.bloomingdales.com/shop/home/bowls-trays-vases?id=1001541'
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'}	
    # ubuntu
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    response = requests.get(url,headers=headers)
    content = BeautifulSoup(response.content,"html.parser")
    
    #print(response.status_code) #helpful when ensuring that connection to webpage successful

    #identify chunk of code that contains page number
    select = content.find('select',attrs={"class":"sort-dropdown-values","id":"sort-pagination-select-top"})
    #pull out the last page number
    try: 
        lastoption = select('option')[-1] #determine the <> that contains total number of pages
        num_of_pages = int(lastoption['value']) +1#convert from string to integer
        #for whatever reason, missing last page count so increment by 1 
    except:
        print('could not find the last option page may not have more than 100 items')
        print(url)
        continue

        #print('num of pages: {}'.format(lastoption['value']))
    print('num of pages var: {}'.format(num_of_pages))

    for eachpage in range(num_of_pages): # to speed up, only it through page 2 and 3
        j = random.random()*2 
        print(j)
        time.sleep(j)
        num_of_pages_ = str(eachpage+1)  #add 1 so that it from 1 to n and not 0 to n-1 in the url
        url2 = prepageIndex[i]+ '/Pageindex/' + num_of_pages_  +CategoryId[i]
         
        #'https://www.bloomingdales.com/shop/home/bowls-trays-vases/Pageindex/' + num_of_pages + '?id=1001541'
        #       "https://www.bloomingdales.com/shop/jewelry-accessories/earrings'   '?id=3628"
        # print(url2)
        # safari 
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0         Safari/605.1.15'} 
        # ubuntu chrome browser 	
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
         
        response = requests.get(url2,headers=headers)
        page_content = BeautifulSoup(response.content,"html.parser") #pull the entire webpage
         
        # write the urls to a file
        f = open(UrlFile, "a")
        f.write('Page '+ str(num_of_pages_) + '\n')
        
        if len(page_content.findAll('a',attrs={"class":"productDescLink"},href=True))==0:
            time.sleep(random.random()*2+1) #attempt to reload page if nothing comes up 
            response = requests.get(url2,headers=headers)
            page_content = BeautifulSoup(response.content,"html.parser") #pull the entire webpage
         
        for item in page_content.findAll('a',attrs={"class":"productDescLink"},href=True): #loop over each thumbnail
            f = open(UrlFile, "a")
            savedUrlinFile= 'https://www.bloomingdales.com' + item['href'] + '\n'
            f.write(savedUrlinFile) #insert url into file 
            print(savedUrlinFile,' saved successfully')
        
    i+=1
