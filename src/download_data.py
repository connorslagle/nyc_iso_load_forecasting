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

def combine_csvs(csvs_dir):


if __name__ == '__main__':
    date_lst = []
    for y in range(2002, 2022):
        for m in range(1, 13):
            if m < 10:
                m_str = '0' + str(m)
            else:
                m_str = str(m)
            date_lst.append(str(y)+m_str+'01')

