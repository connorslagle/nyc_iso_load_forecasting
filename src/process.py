import pdb
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv(
        'data/20130522isolf_20120601isolf_forecasts.csv',
        parse_dates=True,
        index_col=['Time Stamp']
    )
    df = df.drop(columns=['Unnamed: 0'])
    df = df.groupby(df.index).mean()

    # df = pd.read_csv(
    #     'data/20130426palIntegrated_20140217palIntegrated.csv',
    #     parse_dates=True
    # )
    # df = df.drop(columns=['Unnamed: 0'])
    # df_pivot = df.pivot_table(index='Time Stamp', columns='PTID', values='Integrated Load')

    # todo merge dfs, add suffix to forecasts

    pdb.set_trace()