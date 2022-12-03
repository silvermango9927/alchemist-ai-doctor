from flask import Flask, redirect, render_template, url_for, request
from main import runFunc

app = Flask(__name__)

finalDiagnosis = []
summary = []

@app.route('/', methods=['GET', 'POST'])
def home():
	global finalDiagnosis, summary
	if request.method == "POST":
		details = request.form['symptoms']
		finalDiagnosis = runFunc(details)
		if finalDiagnosis == []:
			return render_template('index.html', finalDiagnosis=["Aw man, we couldn't find anything! Try again!"])
		else:
			return render_template('index.html', finalDiagnosis=finalDiagnosis)
	return render_template('index.html', finalDiagnosis=finalDiagnosis)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
