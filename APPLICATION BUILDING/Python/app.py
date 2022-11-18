
from flask import Flask, render_template, request

import joblib

app = Flask (__name__) 

model = joblib.load('wqa_app_.pkl')

@app.route('/')

def home():

	return render_template("home.html")

@app.route('/login',methods = ["POST"])
def login():
	station = request.form["station"]

	loc = request.form["loc"]

	state = request.form["state"]

	temp = request.form["temp"]

	do = request.form["do"]

	ph = request.form["ph"]

	co = request.form["co"]

	bod= request.form["bod"]

	na = request.form["na"]

	tc = request.form["tc"]

	year = request.form["year"]

	total = [[float(tc), float (do), float (ph), float (co), float (bod), float(na)]]

	y_pred = model.predict(total)

	y_pred = y_pred[[0]]

	if(y_pred >= 95 and y_pred<= 100) :

		return render_template("h.html", showcase = 'Excellent, The predicted value is '+str(y_pred))

	elif(y_pred >= 89 and y_pred <= 94) : 

		return render_template("h.html", showcase = 'Very good, The predicted value is '+str(y_pred))

	elif(y_pred >= 80 and y_pred <= 88) : 

		return render_template("h.html", showcase = 'Good, The predicted value is ' +str(y_pred))

	elif(y_pred >= 65 and y_pred <= 79) :

		return render_template("h.html", showcase = 'Fair, The predicted value is '+str(y_pred))

	elif(y_pred >= 45 and y_pred <= 64):

		return render_template("h.html", showcase = 'Marginal, The predicted value is '+str(y_pred))

	else:

		return render_template("h.html", showcase = 'Poor, The predicted value is '+str(y_pred))

if __name__=='_main_':

	app.run(debug=True)