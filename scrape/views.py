from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


# Create your views here.
def index(request):
    url = requests.get('http://saharareporters.com/')
    soup = bs(url.text, 'html.parser')
    title = soup.find_all('div', {'class': 'block-module-content'})
    df = pd.DataFrame()
    for i in title:
        titles = i.find('a').text
        headline = i.find('span').text
        date = i.find_next('div', {'class': 'block-module-content-footer-item-date'}).text.rstrip('\n')

        df = df.append({'Titles': titles, 'Headlines': headline, 'Date': date}, ignore_index=True)
        d = df.head()
    return render(request, 'scrape/index.html', {'d': d})
