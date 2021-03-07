from flask import Flask, render_template, request
import numpy as np
from pygooglenews import GoogleNews
from scraper import getNews
from newspaper import Article

app = Flask(__name__)

def extract(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {"summary": article.summary, "keywords": article.keywords}
    except Exception as e:
        print(e)
        return {"summary": "", "keywords": []}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/energy')
def energy():
    return render_template('energy.html')

@app.route('/pred')
def pred():
    article_obj = extract('https://www.icis.com/explore/resources/news/2021/03/04/10613658/insight-resilient-energy-demand-may-delay-shift-from-fossil-fuels')
    return render_template('pred.html', title='pee pee', link='poo poo',
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))


if __name__ == '__main__':
    app.run(debug=True)