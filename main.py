from flask import Flask, request, jsonify
import csv

all_articles = []

with open('articles.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route('/get-article')

def get_article():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    })

@app.route('/liked-article', methods=['POST'])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(article)
    return jsonify({
        'status' : 'success'
    })

@app.route('/not-liked-article', methods=['POST'])

def not_liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_article.append(article)
    return jsonify({
        'status' : 'success'
    })


if __name__ == '__main__':
    app.run()