from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import time

df_attacker=pd.read_csv('Zone_H_2019_Q3_attacker.csv')
cookie = {'PHPSESSID': 'XXX','ZHE':'YYY'}
print('Scrape is starting...')
for i,attacker in enumerate(df_attacker['Notifier']):
    attacker=attacker.replace(" ", "+")
    attacker=attacker.replace("/", "%252F")
    url='http://www.zone-h.org/archive/filter=1/notifier={}/page=1'.format(attacker)
    response = requests.post(url, cookies=cookie)   
    data = response.text
    soup = BeautifulSoup(data,'lxml')
    data=soup.find("p",{"class":"defaceIntro"}).text.strip()
    Total_Attack=data.split(' ')[2]
    Single_Attack=data.split(' ')[5]
    Mass_Attack=data.split(' ')[9]
    df_attacker.loc[i, 'Total_Attack']=Total_Attack
    df_attacker.loc[i, 'Single_Attack']=Single_Attack
    df_attacker.loc[i, 'Mass_Attack']=Mass_Attack
    
    url='http://www.zone-h.org/archive/filter=1/notifier={}/domain=.nl/page=1'.format(attacker)
    response = requests.post(url, cookies=cookie)   
    data = response.text
    soup = BeautifulSoup(data,'lxml')
    data=soup.find("p",{"class":"defaceIntro"}).text.strip()
    Total_NL_Attack=data.split(' ')[2]
    Single_NL_Attack=data.split(' ')[5]
    Mass_NL_Attack=data.split(' ')[9]
    df_attacker.loc[i, 'Total_NL_Attack']=Total_NL_Attack
    df_attacker.loc[i, 'Single_NL_Attack']=Single_NL_Attack
    df_attacker.loc[i, 'Mass_NL_Attack']=Mass_NL_Attack
    print('{} is finished'.format(attacker))
    time.sleep(2) # Wait for 2 seconds for unblocking the IP
df_attacker.drop(df_attacker.columns[[0, 1]], axis=1, inplace=True)

#calculate the ratio of NL attacks/Total attacks
df_attacker['Ratio']= df_attacker['Total_NL_Attack']/df_attacker['Total_Attack']
df_attacker.sort_values(by ='Ratio',ascending=False, inplace=True)
df_attacker=df_attacker.reset_index(drop=True)

#Saving the data
df_attacker.to_csv('Zone_H_2019_Q3_attacker_detail.csv')     
df_attacker.head()

#Plotting the result
fig=plt.figure(figsize=(40, 12))
xvals = np.arange(df_attacker.shape[0])
plt.bar(xvals, df_attacker['Ratio'],  label='.NL Web Sites')
plt.bar(xvals, 1-df_attacker['Ratio'],  bottom=df_attacker['Ratio'], label='Non .NL Web Sites')

### Dejunkifying Plot
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'left','right']] #Remove top, left and right frame

#Adding Title-Label-Legend
plt.title("An Overview Of The Hackers' Targets\n (whom attacked at least one .NL web site in the first 3Q of 2019) ", size=20)
plt.legend(loc=2, frameon=True)
plt.xticks(xvals, df_attacker['Notifier'],rotation=90, ha='center')

plt.show()