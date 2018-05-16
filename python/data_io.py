import pandas as pd
import numpy as np
import re
import os
from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

'''
Read in data from different sources
read()
read_from_excel()
read_db()
'''

def read(path):
    curdir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(curdir, path)

    if path.lower().endswith('.xlsx'):
        df = pd.read_excel(path)
    elif path.lower().endswith('.csv'):
        df = pd.read_csv(path)

    logger.info('Start to read file {}'.format(os.path.basename(path)))
    return df


def read_dir(dirpath):
    # dirpath = r'C:\Users\syd13065\PycharmProjects\nlpwidg\shangwubu'

    for fl in os.listdir(dirpath):
        if fl.lower().endswith('.xlsx'):
            df = os.path.join(dirpath, fl)
            df = pd.read_excel(df)
    logger.info('Start to read files in dir {}'.format(os.path.basename(dirpath)))
    return df


def read_db():
    from sqlalchemy import create_engine
    engine = create_engine('mysql+pymysql://scq12613:dh628meh21*72K@10.216.200.178:3306/CFP_Bitcoin_DS?charset=utf8')
    df = pd.read_sql_query("SELECT * from announcement", engine)
    return df


if __name__ == '__main__':
    path = r'C:\Users\syd13065\PycharmProjects\nlpwidg\python\shangwubu\small_result.csv'
    # path = r'C:\Users\syd13065\PycharmProjects\nlpwidg\shangwubu\result.xlsx'
    df = read(path)
    print(df.columns)
