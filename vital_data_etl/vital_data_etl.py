# src/etl.py
import pandas as pd
from vital.client import Vital
from vital.environment import VitalEnvironment

def get_vital_data(auth_key, user_id, functions, start_date, end_date):
    client = Vital(api_key=auth_key, environment=VitalEnvironment.SANDBOX)
    data = {}
    for func in functions:
        method = getattr(client.vitals, func)
        function_data = method(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date
        )
        if len(function_data) != 0:
            print(func)
            print(type(function_data))
            data[func] = function_data
    return data

def save_to_csv(data, directory):
    for key, value in data.items():
        final_data = pd.DataFrame([vars(item) for item in value])
        filename = f'{directory}/dataframe_{key}.csv'
        final_data.to_csv(filename, index=False)
