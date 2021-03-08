from flask import Flask, render_template, request
from pipelines import pipeline
import pickle
import numpy as np

nlp = pipeline("e2e-qg", model="valhalla/t5-base-e2e-qg")

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    text = request.form['a']
    pred = nlp(text)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)















