from cgi import test
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import time

url = 'https://www.google.com/search?sxsrf=ALeKk02B-rwjd_voK5Scd2O1FIP-lLKvUg%3A1586500409376&ei=OROQXsPPFpL8kwX0hIaYBQ&q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=google+%D0%BF%D0%BE&gs_lcp=CgZwc3ktYWIQAxgAMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLAToECAAQRzoECAAQQzoCCAA6BAgjECdKFAgXEhA3LTEzN2cxNTFnMzU3Zzg0Sg0IGBIJNy0xZzFnMWc0UJk0WL1CYJNPaABwAngBgAGgA4gBuRCSAQkwLjUuMS4yLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = bs(page.content, 'html.parser')
city = soup.findAll('div', {'class':'wob_loc q8U8x', 'id':'wob_loc'})
week = soup.findAll('div', {'class':'wob_dts', 'id':'wob_dts'})
weather = soup.findAll('span', {'id':'wob_dc'})
tmpr = soup.findAll('span', {'class':'wob_t q8U8x', 'id':'wob_tm'})


city_var = city[0].text #Город
city_var_list = []
city_var_list.append(city_var)

week_var = week[0].text #День недели
week_var_list = []
week_var_list.append(week_var)

weather_var = weather[0].text #Погода
weather_var_list = []
weather_var_list.append(weather_var)

tmpr_var = tmpr[0].text #Температура
tmpr_var_list = []
tmpr_var_list.append(tmpr_var)

test223

def current_weather():

    page = requests.get(url, headers=headers)
    soup = bs(page.content, 'html.parser')

    week = soup.findAll('div', {'class':'wob_dts', 'id':'wob_dts'})
    week_var = week[0].text
    if week_var != week[0].text:
        os.system("cls")
        week_var_list.clear()
        week_var_list.append(week_var)
        print('Город:', city_var_list[0])
        print("День недели:", week_var_list[0])
        print('Погода:', weather_var_list[0])
        print('Температура:', tmpr_var_list[0] + ' °C')

    weather = soup.findAll('span', {'id':'wob_dc'})
    weather_var = weather[0].text
    if weather_var != weather[0].text:
        os.system("cls")         
        weather_var_list.clear()
        weather_var_list.append(weather_var)
        print('Город:', city_var_list[0])
        print("День недели:", week_var_list[0])
        print('Погода:', weather_var_list[0])
        print('Температура:', tmpr_var_list[0] + ' °C')

    tmpr = soup.findAll('span', {'class':'wob_t q8U8x', 'id':'wob_tm'})
    tmpr_var = tmpr[0].text
    if tmpr_var != tmpr[0].text:
        os.system("cls")
        tmpr_var_list.clear()
        tmpr_var_list.append(tmpr_var)
        print('Город:', city_var_list[0])
        print("День недели:", week_var_list[0])
        print('Погода:', weather_var_list[0])
        print('Температура:', tmpr_var_list[0] + ' °C')
    time.sleep(5)#Ждать 5 секунд что бы снова обновиться

try:
    print('Город:', city_var_list[0])
    print("День недели:", week_var_list[0])
    print('Погода:', weather_var_list[0])
    print('Температура:', tmpr_var_list[0] + ' °C')
    while True:
        current_weather()

except:
    quit()




