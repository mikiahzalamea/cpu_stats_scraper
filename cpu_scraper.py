from bs4 import BeautifulSoup
import requests
import pandas as pd

# Scrape the page
url = "https://www.cpubenchmark.net/cpu_value_available.html"

# Make the request
response = requests.get(url)

# Parse the response
soup = BeautifulSoup(response.text, "html.parser")

# Save the results under an html to view
with open ("cpu_ratings.html", "w") as file:
     file.write(str(soup.prettify()))

#For the product names list
product_list = soup.find_all('span', {'class': 'prdname'})
product_names = [product.text for product in product_list]

# CPU Mark / Price List
score_list = soup.find_all('span', {'class': 'count'})
score_names = [score.text for score in score_list]

# CPU Mark
cpu_mark_list = soup.find_all('span', {'class': 'mark-neww'})
cpu_mark_names = [cpu_mark.text for cpu_mark in cpu_mark_list]

# CPU Price
cpu_price_list = soup.find_all('span', {'class': 'price-neww'})
cpu_price_names = [cpu_price.text for cpu_price in cpu_price_list]

# Concatenate the 4 Lists into a DataFrame
df = pd.DataFrame({'Product': product_names, 'Score': score_names, 'CPU Mark': cpu_mark_names, 'CPU Price': cpu_price_names})

print(df)