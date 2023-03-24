# Amazon-products-info-scraping-using-python-and-BeautifulSoup
It is an excellent exercise to work on web scraping using beautiful soup.

## Task list

### Part 1

- [x] Scrape all products from the given url.

- [x] Scraped 20 pages of product listing pages. One of the 20 pages/page example: 
https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2 C283&ref=sr_pg_1

- [x] Saved the extracted data into a .csv file.

Scraped items include: 
- [x] Product URL,
- [x] Product Name,
- [x] Product Price,
- [x] Rating,
- [x] Number of reviews.

### Part 2

- [x] 200 products data has been extracted.

 Scraped items include: 
- [x] Product Name,
- [x] Description,
- [x] ASIN,
- [x] Product Description,
- [x] Manufacturer.


### Output
- [x] Save the part1 extracted data(426 products, i.e., 20 pages products) in a .csv file.
- [x] Save the part2 extracted data(first 200 products of the above 426 products, as mentioned) in a .csv file.
- [x] Save the entire data(first 200 products of the above 426 products, part1+part2) in a .csv file. [This is the final file and it's supposed to be submitted.]
- [x] The entire data exported in a .csv format.

### NOTE
- [x] NOTE: PYTHON PROGRAMMING IS USED TO EXTRACT DATA FROM THE URLs.
- [x] NOTE: BEAUTIFULSOUP IS USED FOR DATA CRAWLING. 





## Instructions:

Macbook is used to develop the code. Running the files in systems other than macOS requires attention to the directories and paths provided.

Unzip the webpages file. The resulting folder contains 40 files, including 20 .html files and 20 folders with corresponding page items like images and other files.

Make sure all the files, i.e., part1.py, part2.ipynb, webpages folder, is in a directory(folder) named "00Analystt.ai".

Run the part1.py file in 'atom' or any other IDE you prefer. Running this code will create the 'part1' '.csv' file named "Part 1_20_pages_products.csv".

Run the part2.ipynb in 'Jupiter notebook'. Use Jupiter notebook to utilise the URL links in the part1.csv file. Running this code creates a 'part2' '.csv' file named "Part_2_products_info.csv".


## Challenges I faced:

A few pages have different layouts. 

Some elements I wanted to extract do not have any grip, unlike others with classes and ids' in their tags.

Ensure 'user Agent' in 'headers' is valid and suits the current use case.
