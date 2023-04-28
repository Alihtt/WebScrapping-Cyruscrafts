from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests


workbook = Workbook()
worksheet = workbook.active

url = "https://www.cyruscrafts.com/categories/18/accessory?resultsPerPage=99999"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
sub_pages = soup.find_all("div", class_="js-product-miniature-wrapper")

worksheet.append(
    ["ID", "Title", "Price", "Description", "Page Url", "Image url"])

for sub_page in sub_pages:

    product_id = sub_page.find(
        class_="product-description")("div", class_="product-reference")[0]("a")[0].contents[0]
    title = sub_page.find(
        class_="product-description")("h2")[0]("a")[0].contents[0]
    price = "$" + "{:.2f}".format(float(sub_page.find(
        class_="product-description")("span")[0].attrs["content"]))
    description = sub_page.find(
        class_="product-description")("div", class_="product-description-short text-muted")[0]("a")[0].contents[0]
    url = sub_page.find(
        class_="product-description")("h2")[0]("a")[0].attrs["href"]
    img_url = sub_page.find(
        class_="thumbnail-container")("a")[0]("img")[0].attrs["data-src"]

    worksheet.append([product_id, title, price, description, url, img_url])


workbook.save("data.xlsx")
