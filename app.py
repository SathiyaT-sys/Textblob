from flask import Flask,render_template,request
from textblob import TextBlob
from nltk.sentiment import SentimentAnalyzer

app = Flask(__name__)   

def sentiment_analyzer(text):
    sentiment= TextBlob(text)
    score= sentiment.sentiment.polarity
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

@app.route('/', methods=['GET','POST'])
def index():
    sentiment = None
    if request.method=="POST":
     text= request.form['text']
     sentiment = sentiment_analyzer(text)
    return render_template('index.html',sentiment=sentiment)

if __name__=='__main__':
    app.run(debug=True)
