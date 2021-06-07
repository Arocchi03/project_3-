# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func

from flask import Flask, jsonify, Response, render_template, request
import joblib
#import sklearn
import pandas as pd
#from flask_cors import CORS

# Flask set up
app = Flask(__name__)
#CORS(app)

#load the machine learning model
model = joblib.load('TestModel.sav')

# Routes
@app.route("/")
def index():
	return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
	x_tmin = float(request.form['tmin'])
	x_tmax = float(request.form['tmax'])
	x_prcp = float(request.form['prcp'])
	x_snow = float(request.form['snow'])
	x_wspd = float(request.form['wspd'])
	new_input = [[x_tmin, x_tmax, x_prcp, x_snow, x_wspd]]
	#new_output = 2.2*x_tmin + 1.7*x_tmax + 10*x_prcp + 3*x_snow + 3*x_wspd
	new_output = model.predict(new_input)
	#return 'Number of crimes: '+ .$new_output[0]. +'<br><br><a href="/">Back Home</a>'
	return 'Number of crimes: '+ repr(new_output[0])+'<br><br><a href="/">Back Home</a>'
    #return 'Estimated crime is %s <br/> <a href="/">Back Home</a>' % (new_output)

if __name__ == '__main__':
	app.run()
#    app.run(debug=True)