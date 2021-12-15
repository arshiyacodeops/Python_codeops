import requests
import pandas as pd
import matplotlib.pyplot as plt

# Documentation is in: https://api-test.sandbox-resellers.jetbrains.com/doc/
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Api-Key': '4nm408j6l98hpnfi71kzqxcnc'
}
response = requests.get(
    'https://api-test.sandbox-resellers.jetbrains.com/resellers/api/v1/productPrices', headers=headers)
print(response.text)

df = pd.json_normalize(response.json())

df.to_csv("test.csv")

df.to_excel('test.xlsx')

df.to_html('test.html')

x = pd.read_csv("test.csv")
x.drop(columns='Unnamed: 0', inplace=True)

x['suggestedPrice.value'].plot.kde()
plt.show()

plt.boxplot(x['resellersPrice.value'])
plt.show()
plt.figure(figsize=(7, 7))
plt.scatter(x['resellersPrice.value'], x['suggestedPrice.value'])
plt.xlabel("resellersPrice.value")
plt.ylabel("suggestedPrice.value")
plt.show()
