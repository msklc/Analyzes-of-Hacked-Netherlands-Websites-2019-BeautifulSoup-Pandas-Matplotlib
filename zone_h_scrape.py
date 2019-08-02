from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime
import calendar

df=pd.DataFrame()
start_date = pd.to_datetime('2019/01/01')
print('Scrape is starting...')
cookie = {'PHPSESSID': 'epbati0m8mjv8j0eu4tkn8tlc0','ZHE':'9761f39e14f84791346a2ae3398c1db3'}
page_no=1
finish_date=pd.to_datetime('today')
date_07=pd.to_datetime('2019/07/31')

while finish_date>start_date:
#while page_no<3:
    url='http://www.zone-h.org/archive/filter=1/published=0/domain=.nl/fulltext=1/page={}'.format(page_no)
    print(url)
    response = requests.post(url, cookies=cookie)
    data = response.text
    soup = BeautifulSoup(data,'lxml')

    for tr in soup.select('tr')[:-2]:
        row = []
        for td in tr.select('td'):
            if td.text.strip():
                row.append(td.text.strip())
            else:
                img = td.select_one('img[title]')
                if img:
                    row.append(img['title'])
                else:
                    row.append('')
            a = ["0" if x == '' else x for x in row] #cleaning the NaN values as 0
        df = df.append([a])
    print('Page {} is complete'.format(page_no))
    page_no+=1
    df[0] = pd.to_datetime(df[0], errors='coerce', format='%Y/%m/%d') #Arrange the Time column
    finish_date=df.nsmallest(1,columns = 0)[0][0] #find the smallest date for continuing to loopp
else:
#Set first row as header
    df.columns = df.iloc[0]
    df = df[1:]
    df.rename(columns={ df.columns[0]: "Time",df.columns[5]: "S_Location",df.columns[6]: "Special" }, inplace = True)
    df["S_Location"] = df["S_Location"].replace("0", "Unknown")#Set the location value of 0 to Unknown
    df["R"] = df["R"].replace("R", "1")#Set the ReAttack value of R to 1
    print('Scrape the data of 2009 is finish')
    df = df[df.Time >= start_date] #eliminate the data before '2019/01/01'
    df = df[date_07>= df.Time] #eliminate the data before '2019/07/31'
    df=df.reset_index(drop=True)
df.to_csv('Zone_H_{}.csv'.format(datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')))#Save as csv file
print('The data is ready!')