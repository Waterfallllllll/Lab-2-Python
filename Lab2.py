
import csv
from bs4 import BeautifulSoup

with open("index.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

page_temp = soup.find_all("td", class_="first_in_group positive")
page_data = soup.find_all("td", class_="first")
page_pressure = soup.find_all("td", class_="pressure")
page_wind = soup.find_all("span", class_="wind")

with open("dataset.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    for date, temp, pressure, wind in zip(page_data, page_temp, page_pressure, page_wind):
        writer.writerow([date.text, temp.text, pressure.text, wind.text])

