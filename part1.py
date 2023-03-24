from bs4 import BeautifulSoup
import csv

import urllib.parse #to work with URLs

from urllib.parse import urlparse, urlunparse

# create a list of HTML file names
i=1
html_files = []
while i<21:
  html_files.append('webpages/page{}.html'.format(i))
  i+=1


# open a csv file to write the data
with open('20_pages_products.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # write the header row
    writer.writerow(['Product Name', 'Product URL', 'Product Price(\u20B9)', 'Product Rating', 'Product Number of Reviews'])

    # loop through each HTML file
    for file_name in html_files:
        # open the HTML file
        with open(file_name, 'r') as f:
            # read the content of the file
            content = f.read()

        # parse the content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # find all divs with class "sg-col-inner"
        divs = soup.find_all('div', class_="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right")

        # loop through each div
        for div in divs:
            # try to find the product name
            product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal')
            if product_name:
                product_name = product_name.text.strip()
            else:
                product_name = ""

            # try to find the product url
            product_url = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
            if product_url:
                product_url = product_url['href']
                url = product_url

                parsed_url = urlparse(url) # Parse the URL into its components
                # Rebuild the URL to ensure it has the necessary components
                standard_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, parsed_url.query, ''))

                # url = product_url
                #
                # # Decode the URL
                # decoded_url = urllib.parse.unquote(url)
                #
                # # Extract the product URL from the query string, if available
                # query_params = urllib.parse.parse_qs(urllib.parse.urlparse(decoded_url).query)
                # if "url" in query_params:
                #     product_url = urllib.parse.unquote(query_params["url"][0])
                # else:
                #     # If 'url' is not available in the query string, extract the product URL from the path
                #     path_parts = urllib.parse.urlparse(decoded_url).path.split('/')
                #     product_url = "/".join(part for part in path_parts if part != '')
                #
                #
                # product_url = 'https://www.amazon.in/'+product_url
                #
                # if product_url[-len('_sspa?crid=2M096C61O4MLT'):] != '_sspa?crid=2M096C61O4MLT':
                #     product_url += '_sspa?crid=2M096C61O4MLT'


            else:
                product_url = ""

            # try to find the product price
            product_price = div.find('span', class_='a-price-whole')
            if product_price:
                product_price = product_price.text.strip()
            else:
                product_price = ""

            # try to find the product rating
            product_rating = div.find('span', class_='a-size-base')
            if product_rating:
                product_rating = product_rating.text.strip()
            else:
                product_rating = ""

            # try to find the product number of reviews
            product_no_of_reviews = div.find('span', class_='a-size-base s-underline-text')
            if product_no_of_reviews:
                product_no_of_reviews = product_no_of_reviews.text.strip()
            else:
                product_no_of_reviews = ""

            # write the product data to the csv file
            writer.writerow([product_name, product_url, product_price, product_rating, product_no_of_reviews])
