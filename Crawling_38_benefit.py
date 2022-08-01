
# url = 'http://www.38.co.kr/html/fund/?o=v&no=1796'
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import numpy as np


def crawling_38_benefit():
    df_dic = {}
    df_dic['기업명'] = []
    df_dic['시초/공모%(수익률)'] = []



    for p in range(1,65+1): # page num
    #     print('page : ',p)
        base_url = f'http://www.38.co.kr/html/fund/index.htm?o=nw&page={p}'
        html = ur.urlopen(base_url)
        soup = bs(html.read(), "html.parser")


        if soup is None:
            break
        
        if p == 1:
            table = soup.find_all('tr',bgcolor='#FFFFFF')[1:]
        else:
            table = table = soup.find_all('tr',bgcolor='#FFFFFF')
        table2 = soup.find_all('tr',bgcolor='#F8F8F8')
        for i in table:
            name = i.find('a').text

            benefit = i.find_all('td')[-3].text
            df_dic['기업명'].append(name)
            df_dic['시초/공모%(수익률)'].append(benefit)

        for i in table2:
            name = i.find('a').text
            benefit = i.find_all('td')[-3].text
            df_dic['기업명'].append(name)
            df_dic['시초/공모%(수익률)'].append(benefit)
    df_benefit = pd.DataFrame(df_dic)     
    df_merge_benefit = pd.merge(df,df_benefit,on='기업명')
    df_merge_benefit.to_csv('38com_benefit.csv', mode='a')