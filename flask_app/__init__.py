from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000/
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    arr = np.array([[data1, data2, data3]])
    pred = model.predict(arr)
    return render_template('predict.html', data=pred)

if __name__ == '__main__':
    app.run(debug=True)

# FLASK_APP=flask_app flask run