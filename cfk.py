#! python3
import bs4, requests, time, os

switch = False
getPage = requests.get("https://studycoin.kfc.ro/")
getPage.raise_for_status()


text = bs4.BeautifulSoup(getPage.text, 'html.parser')
iteme = text.select('.tickerItem')


what_i_want = '1 studycoin'
flength = len(what_i_want)


for x in iteme:
    for i in range(len(x.text)):
        chunk = x.text[i:i+flength].lower()
        if chunk == what_i_want:
            value = x.text[i+flength+3:i+flength+7].lower()
            if float(value) >= 0.4:
                switch = True

print(switch)
if switch == True:
    os.system("start cmd")
print(value)
 	
