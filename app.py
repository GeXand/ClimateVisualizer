from flask import Flask, render_template, request
import numpy as np
from pygooglenews import GoogleNews
from scraper import getNews
from newspaper import Article
import nltk

nltk.download('punkt')

app = Flask(__name__)

def extract(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return {"summary": article.summary, "keywords": article.keywords}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/energy')
def energy():
    return render_template('energy.html')

@app.route('/pred')
def pred():
    news = {'title': 'INSIGHT: Resilient energy demand may delay shift from fossil fuels - ICIS',
 'href': 'https://www.icis.com/explore/resources/news/2021/03/04/10613658/insight-resilient-energy-demand-may-delay-shift-from-fossil-fuels'}
    #news = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)
    curArticle = news
    article_obj = extract(curArticle['href'])
    return render_template('pred.html', title=curArticle['title'], link=curArticle['href'], 
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))


if __name__ == '__main__':
    app.run(debug=False)