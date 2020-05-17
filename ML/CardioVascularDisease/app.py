# Serve model as a flask application

import pickle
import numpy as np
from flask import Flask, request
from flask import Flask, request, jsonify, render_template, url_for
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
standard_x = StandardScaler()
model = pickle.load(open('CardiovascularDisease_model.pkl', 'rb'))


@app.route('/')
def home_endpoint():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    standard_value = standard_x.fit_transform(final_features)
    prediction = model.predict(standard_x.transform(standard_value))

    output = prediction[0]
    if(output==0):
        return render_template('index.html', prediction_text='cardiovascular disease is Inactive')
    else:
        return render_template('index.html', prediction_text='cardiovascular disease is Active')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)
    standard_value = standard_x.fit_transform([np.array(list(data.values()))])
    prediction = model.predict(standard_x.transform(standard_value))

    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    #load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=8080)
