import pandas as pd
import numpy as np
import re
import os
import datetime

from data_io import read, read_dir, read_db
from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

'''
Dataframe preprocessing
'''

def news_df(df):
    '''
    Read in the scraped data --> excel/DB

    :return: dateframe
    '''
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    #     writer = pd.ExcelWriter(r'C:\Users\syd13065\Desktop\shangwubu\result.xlsx')
    #     df.to_excel(writer, 'Sheet1')
    #     writer.save()

    # original len(df) is 2366
    # len(df.content) = 2111
    logger.info('Preprocessing the dataframe')
    return df

if __name__ == '__main__':
    # df = read_dir('C:/Users/syd13065/Workspaces/bcevent/data/')
    path = r'C:\Users\syd13065\PycharmProjects\nlpwidg\shangwubu'
    df = read_dir(path)
    df = news_df(df)
    print(len(df))
