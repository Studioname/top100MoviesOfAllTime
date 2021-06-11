from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
website_data = response.text
soup = BeautifulSoup(website_data, "html.parser")

data = soup.find_all(name="h3", class_ = "title")

movies = []

try:
    file = open("movies_list.txt", "w")

except:
    file = open("movies_list.txt", "w")

finally:

    for entry in data[::-1]:
        text = str(entry.getText() + "\n")
        file.write(text)
file.close()