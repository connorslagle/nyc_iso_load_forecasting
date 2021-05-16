import pandas as pd

if __name__ == '__main__':
    # df = pd.read_csv(
    #     'data/20130522isolf_20120601isolf_forecasts.csv',
    #     parse_dates=True,
    #     index_col=['Time Stamp']
    # )
    df = pd.read_csv(
        'data/20130426palIntegrated_20140217palIntegrated.csv',
        parse_dates=True,
        index_col=['Time Stamp']
    )
    df = df.drop(columns=['Unnamed: 0'])


    pdb.set_trace()