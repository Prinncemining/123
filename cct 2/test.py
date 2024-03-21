import os
try:
 import cloudscraper
except:
 os.system('pip install cloudscraper')
whisper = cloudscraper.create_scraper( 
    browser={ 
        'browser': 'chrome', 
        'platform': 'windows', 
        'desktop': True 
    } 
)
#You Can Use All Requests Library Methods (Post,Get,Options...etc)
response=whisper.post('https://rewards.bing.com/redeem/checkout/').text
print(response)