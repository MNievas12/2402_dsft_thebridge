from fake_useragent import UserAgent
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url, headers=headers)
soup = bs(response.content, 'html.parser')


dict_peliculas = {}
dict_peliculas['ranking'] = [x.get_text().split(" ", 1)[0][:-1] for x in soup.find_all("h3")[1:251]]
dict_peliculas['titulos'] = [x.get_text().split(" ", 1)[1] for x in soup.find_all("h3")[1:251]]
dict_peliculas['año'] = [x.get_text() for x in soup.find_all("span", class_="sc-be6f1408-8 fcCUPU cli-title-metadata-item") if len(x.get_text()) == 4]
dict_peliculas['duracion'] = [x.find_all("span")[1].get_text() for x in soup.find_all("div", class_="sc-be6f1408-7 iUtHEN cli-title-metadata")]
dict_peliculas['rating'] = [x['aria-label'][-3:] for x in soup.find_all("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")]
df = pd.DataFrame(dict_peliculas)

df.to_csv("data/imdb_top250_" + str(datetime.now())[:10] + ".csv")
