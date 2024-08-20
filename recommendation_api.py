from flask import Flask, request, jsonify
from sistem_rekomendasi_film import film_recommendations
import pandas as pd
import pickle

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

df1 = pd.read_csv('tmdb_5000_movies.csv')

tf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))

@app.route('/api/', methods=['POST'])

def recommend():
    title = request.json['title']
    recommendations = film_recommendations(title)
    return jsonify({'title': title, 'recommendations': recommendations.to_dict()}), 200

if __name__ == '__main__':
    app.run(debug=True)