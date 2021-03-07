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
    article_obj = extract('https://www.theguardian.com/environment/2020/aug/31/australias-big-polluters-required-to-offset-just-12-of-greenhouse-gas-emissions-in-past-year%27')
    return render_template('pred.html', title='pee pee', link='poo poo',
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))


if __name__ == '__main__':
    app.run(debug=False)