import json

import pandas as pd
import pdfkit
import requests
from bs4 import BeautifulSoup

#PDF document generation library for Node

pages = []
for i in range(1, 101):
    pages.append('https://collectionapi.metmuseum.org/public/collection/v1/objects/{}'.format(i))
    main_df = pd.DataFrame()

for i in pages[0:50]:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, 'html5lib')
    dct = dict(json.loads(soup.body.text))
    main_df = main_df.append(pd.DataFrame.from_dict(dct, orient='index').transpose(), ignore_index=True)
print(response)

main_df.to_csv("main_df.csv")
main_df.to_excel('main_df.xlsx')
main_df.to_html('main_df.html')

csv = 'main_df.csv'
html_file = csv[:-3] + 'html'

df = pd.read_csv(csv, sep=',')
df.to_html(html_file)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

#wkhtmltopdf is used to convert html file to pdf

pdfkit.from_url("main_df.html", "FinalOutput.pdf", configuration=config)


print(main_df)