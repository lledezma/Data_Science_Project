import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'Tripadvisor': 'http://tripadvisor.com/',
         'Trivago':'http://www.trivago.com/',
         'Hotels': 'http://www.hotels.com/'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()

