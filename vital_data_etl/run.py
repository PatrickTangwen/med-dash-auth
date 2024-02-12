# run.py
import json
from vital_data_etl import get_vital_data, save_to_csv

def main():
    print("program is running")
    with open('etl.json') as json_file:
        config = json.load(json_file)
    
    auth_key = config['auth_key']
    user_id = config['user_id']
    functions = config['functions']
    start_date = config['start_date']
    end_date = config['end_date']
    directory = config['directory']
    
    data = get_vital_data(auth_key, user_id, functions, start_date, end_date)
    save_to_csv(data, directory)
if __name__ == "__main__":
    main()
