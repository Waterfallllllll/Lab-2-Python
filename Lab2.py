
import csv
from bs4 import BeautifulSoup

# # pip install requests-html
# from requests_html import HTMLSession

# session = HTMLSession()
# rs = session.get('https://www.gismeteo.ru/diary/4980/2023/9/')
# with open('rs_before_js.html', 'w', encoding='utf-8') as f:
#     f.write(rs.html.html)

# rs.html.render()  # Без этого не будет выполнения js кода

# with open('rs_after_js.html', 'w', encoding='utf-8') as f:
#     f.write(rs.html.html)

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

