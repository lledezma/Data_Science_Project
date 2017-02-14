import requests
from bs4 import BeautifulSoup


urlTrivago = 'http://www.trivago.com/?iPathId=34741&bDispMoreFilter=false&aDateRange%5Barr%5D=2017-02-19&aDateRange%5Bdep%5D=2017-02-20&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&iRoomType=7&sOrderBy=relevance%20desc&aPartner=&aOverallLiking=1%2C2%2C3%2C4%2C5&iOffset=0&iLimit=25&iIncludeAll=0&bTopDealsOnly=false&iViewType=0&aPriceRange%5Bto%5D=0&aPriceRange%5Bfrom%5D=0&aGeoCode%5Blng%5D=-115.17292&aGeoCode%5Blat%5D=36.112774&bIsSeoPage=false&aHotelTestClassifier=&bSharedRooms=false&bIsSitemap=false&rp=&cpt=3474103&iFilterTab=0&'
pageTrivago = requests.get(urlTrivago)


soupTrivago = BeautifulSoup(pageTrivago.content, 'lxml')


position = soupTrivago.find('article')
hotelname = position.find('div', class_='item__details').find('span').string
hoteladdress= position.find('span', class_='item__distance').string
hotelprice = position.find('div', class_='item__best-details ').find('strong').string
hotelrating = position.find('em', class_='item__rating-number fs-normal').find('span').string
hotelreviews= position.find('span',class_='review__count').string


print('Name:',hotelname)
print('Address:',hoteladdress)
print('Price:',hotelprice)
print('Rating:',hotelrating)
print('Reviews:',hotelreviews)

