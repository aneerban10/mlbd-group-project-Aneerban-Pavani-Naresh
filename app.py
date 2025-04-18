from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load model and data once
with open("SVD_Recommender.pkl", "rb") as f:
    model = pickle.load(f)

complete_df = pd.read_csv("Collaborative-Filtering-Dataset/Book_Ratings.csv")  # Local or GCS-downloaded CSV

app = Flask(__name__)

def recommend_books(user_id, n=10):
    all_books = complete_df['Book-Title'].unique()
    rated_books = complete_df[complete_df['User-ID'] == user_id]['Book-Title'].values
    books_to_predict = [book for book in all_books if book not in rated_books]
    
    predictions = []
    for book in books_to_predict:
        pred = model.predict(user_id, book)
        predictions.append((book, pred.est))

    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:n]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_id = int(request.form["user_id"])
        recommendations = recommend_books(user_id)
        return render_template("recommendations.html", user_id=user_id, recommendations=recommendations)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
