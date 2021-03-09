from flask import Flask, render_template, request

from pipelines import pipeline

app = Flask(__name__)

model = pipeline("question-generation")

@app.route('/')
def index():
	return render_template("index.html", data="hey")


@app.route("/qselect", methods=["POST"])
def qselect():
	text = request.form['sometext']
	data = model(text)
	return render_template("q-select.html", data=data, text=text)


if __name__ == "__main__":
	app.run(debug=True, use_reloader=False)
