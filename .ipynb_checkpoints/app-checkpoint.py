from flask import Flask, render_template, request

from pipelines import pipeline

app = Flask(__name__)

model = pipeline("question-generation")

@app.route('/')
def index():
	return render_template("index.html", data="hey")


@app.route("/prediction", methods=["POST"])
def prediction():
	text = request.form['sometext']

	data = model(text)

	return render_template("prediction.html", data=data)


if __name__ == "__main__":
	app.run(debug=True, use_reloader=False)