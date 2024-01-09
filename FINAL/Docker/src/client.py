import pandas as pd
import numpy as np
import requests
import math
from sklearn import metrics
from pathlib import Path

def print_metrics(y_test, y_test_predict):
    print('Valid R^2: {:.3f}'.format(metrics.r2_score(y_test, y_test_predict)))
    print('Valid MAPE: {:.3f}'.format(metrics.mean_absolute_percentage_error(y_test, y_test_predict)*100))
    print('RMSE: {:.3f}'.format(math.sqrt(metrics.mean_squared_error(y_test, y_test_predict))))

if __name__ == '__main__':
    outpath = Path.cwd() / ("libs") / ("data_valid.csv")
    df = pd.read_csv(str(outpath))
 
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost:5000/predict', json=df.to_json())
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200)
        y_pred = np.array(r.json()['prediction'])
        y_valid = np.array(r.json()['prediction2'])
               
        # Выводим результирующие метрики
        print_metrics(np.exp(y_valid), np.exp(y_pred))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)