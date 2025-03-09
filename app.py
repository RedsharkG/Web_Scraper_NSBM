# Redshark
# Sehara Gishan Samarasinghe
# Created : 9th May of 2025

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
def get_news():
    url = 'https://www.nsbm.ac.lk/category/news/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    articles = soup.find_all('article', class_='category-news')
    news_list = []

    for news in articles:
        title = news.find('h2', class_='entry-title').text.strip()  # Grabbing Title 
        
        # Try getting image from data-src first (for lazy-loaded images)
        image_tag = news.find('img', class_='wp-post-image')
        image = image_tag['data-src'] if image_tag and image_tag.has_attr('data-src') else image_tag['src'] if image_tag else None
        
        news_list.append({'title': title, 'image': image})

    return jsonify(news_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
