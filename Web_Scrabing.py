import gspread
import pandas as pd
import regex as re
import requests
from bs4 import BeautifulSoup
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
url = "https://www.goodreads.com/shelf/show/100-books-to-read-before-you-die"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# Find top 5 rated authors spreadsheet
data_frame = {}
for rating, author in zip(soup.findAll("div", {"class": "left"}),
                          soup.findAll("div", {"class": "authorName__container"})):
    data_frame[author.text[1:][:-2]] = str(re.findall(pattern=r'avg rating \d{1}.\d{2}',
                                             string=str(rating.find("span", {"class": "greyText smallText"}))))[-6:-2]

f = sorted(data_frame.items(), key=lambda item: item[1], reverse=True)[:5]
df = pd.DataFrame(f, columns=['Author', 'Average Rating'])

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'jsonFileFromGoogle.json', scope)
gc = gspread.authorize(credentials)
#Create a Google Form
spreadsheet_key = '17DeaxJHYT3yews6f9UsmvIZzPYoCXVrrbxkPI4I4BO8'
wks_name = 'Automation'
d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)
