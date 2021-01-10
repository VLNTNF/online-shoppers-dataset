from flask import Flask, request, jsonify, render_template
import pickle

import module_preprocessing

app = Flask(__name__)
model = pickle.load(open('onlineShopper_model.pickel','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	'''
	For rendering results on HTML GUI
	'''
	features = [x for x in request.form.values()]
	#features = [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,1,"Returning_Visitor","False"]
	final_features = module_preprocessing.datapreprocessing([features])
	prediction = model.predict(final_features)

	output = prediction[0]

	if output==1:
		output= True
	else:
		output = False

	return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')