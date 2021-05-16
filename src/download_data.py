import pdb
from zipfile import ZipFile

import pandas as pd
import os
import requests


def download_iso_data(date_str, forecasts=False):
    if forecasts:
        zip_url = f'http://mis.nyiso.com/public/csv/isolf/{date_str}isolf_csv.zip'
        zip_file = f'data/archives/forecasts/{date_str}.zip'
    else:
        zip_url = f'http://mis.nyiso.com/public/csv/palIntegrated/{date_str}palIntegrated_csv.zip'
        zip_file = f'data/archives/actual/{date_str}.zip'

    response = requests.get(zip_url)
    with open(zip_file, 'wb') as f:
        f.write(response.content)

def unzip_archive(zip_file_path, extract_path):
    try:
        with ZipFile(zip_file_path) as f:
            f.extractall(path=extract_path)
    except BaseException:
        pass

def combine_csvs(csvs_dir, suffix, save_df=False):
    csv_list = os.listdir(csvs_dir)
    first_file, last_file = csv_list[0].split('.csv')[0], csv_list[-1].split('.csv')[0]

    df = pd.DataFrame()
    for f in csv_list:
        if f.endswith('.csv'):
            f_df = pd.read_csv(f'{csvs_dir}{f}')
            df = df.append(f_df)
    if save_df:
        df.to_csv(f'data/{first_file}_{last_file}_{suffix}.csv')
    return df


if __name__ == '__main__':
    pdb.set_trace()
