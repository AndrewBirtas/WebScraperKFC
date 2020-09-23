#! python3
import bs4, requests, time, os

switch = False
getPage = requests.get("https://studycoin.kfc.ro/")
getPage.raise_for_status()


text = bs4.BeautifulSoup(getPage.text, 'html.parser') #get html
iteme = text.select('.tickerItem') #get desired item class from html


what_i_want = '1 studycoin'
flength = len(what_i_want)

#search for the exact item
for x in iteme:
    for i in range(len(x.text)):
        chunk = x.text[i:i+flength].lower()
        if chunk == what_i_want:
            value = x.text[i+flength+3:i+flength+7].lower()
            if float(value) >= 0.4:
                switch = True

print(switch)
if switch == True:
    os.system("start cmd") #do something if the value is true!
print(value)
 	
