
import pandas as pd
import pickle
from flask import Flask, request, jsonify

import sys, os
sys.path.append(os.path.join(os.path.abspath(''), '..', 'libs'))

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

@app.route('/predict', methods=['POST'])
def predict_func():    
    # загружаем модель из файла
    with open('/src/app/libs/model.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)
    # features = request.json
    df = pd.read_json(request.json, dtype={str})  
    df_x = df.drop('target', axis=1)
    y_pred = model.predict(df_x)   
    y_valid = df['target']
    return jsonify({'prediction': y_pred.tolist(), 'prediction2': y_valid.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)