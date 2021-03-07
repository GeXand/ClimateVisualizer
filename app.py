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

@app.route('/pred')
def pred():
    news = getNews("carbon emissions OR greenhouse gas OR co2 emissions", max_articles=20)
    curArticle = news[4]
    article_obj = extract(curArticle['href'])
    return render_template('pred.html', title=curArticle['title'], link=curArticle['href'],
                           summary=article_obj['summary'], keywords=', '.join(article_obj['keywords']))


if __name__ == '__main__':
    app.run(debug=False)