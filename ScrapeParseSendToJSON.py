import requests
import datetime
from bs4 import BeautifulSoup
import json

# Create dict for JSON Object
response = []

# Prepare for parsing with BeautifulSoup
urlAPNewsBriefs = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
today = str(datetime.datetime.now().date())
for position in soupAPNewsBriefs.find_all('div', class_='ap-newsbriefitem'):
    if position.find('a'):
        headline = position.find('a').string
        fullStory = 'http://hosted.ap.org/' + position.find('a').get('href')
        ctime = fullStory.split('CTIME=')[1]
    if position.find('span', class_='topheadlinebody'):
        brief = position.find('span', class_='topheadlinebody').string
        apOffice = brief.split(' (AP)')[0]

    # Make changes to response 
    response.append({'Headline': headline, 'Brief': brief, 'AP_Office': apOffice, 'Full_Story': fullStory,
                     'CTIME': ctime})

# Write response to JSON file
postingsFile = '/Users/admin/Dropbox/CSC3130/WebProject/SchTasks/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()