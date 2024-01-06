import pandas as pd
import numpy as np
links=pd.read_csv("links.csv")
ratings=pd.read_csv("/ratings.csv")
filtered_links = ratings.groupby('userId').filter(lambda x: len(x) > 50)
use_data=pd.merge(filtered_links,links,on="movieId",how="inner")
use_data.drop("userId",axis=1,inplace=True)
condition = use_data['rating'] < 5.0
use_data = use_data.drop(use_data[condition].index)
a=use_data[["imdbId","movieId"]]
a=a.drop_duplicates()
a=a.head(100)
import nest_asyncio
nest_asyncio.apply()

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

async def fetch_imdb_rating(session, imdb_id):
    id = str(int(imdb_id))
    n_zeroes = 7 - len(id)
    new_id = "0" * n_zeroes + id
    url = f"https://www.imdb.com/title/tt{new_id}/"
    headers = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    retries = 30
    for attempt in range(retries):
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    imdb_rating = soup.find('span', attrs={'class': 'sc-bde20123-1 cMEQkK'})
                    return imdb_rating.text if imdb_rating else None
                else:
                    return None
        except aiohttp.ClientConnectionError:
            print(f"Attempt {attempt + 1}/{retries}: Connection error. Retrying...")
            await asyncio.sleep(2)

    return None

async def loop_data_async(imdb_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_imdb_rating(session, imdb_id) for imdb_id in imdb_ids]
        imdb_ratings = await asyncio.gather(*tasks)
        return imdb_ratings

def loop_data():
    imdb_ids = a["imdbId"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(loop_data_async(imdb_ids))
    finally:
        loop.close()
a["Imdb_ratings"]= loop_data()

a.head(100)
