import pandas as pd
import os
import re
from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

def futures_count(lst):
    '''
    Given a list of keywords,
    Return the count of given list of futures
    :param lst:
    :return:
    '''
    logger.info('Count the keywords in the list of futures')
    path = os.path.dirname(__file__) + r'\..' + r'\data\手续费调整.xls'

    df = pd.read_excel(path)
    #     df.dropna(subset=['品种名称'], inplace=True)
    df = df[pd.notnull(df['品种名称'])]
    res = df['品种名称'].tolist()

    dct = {}
    dct = {x: dct.get(x, 0) for x in res}
    for el in lst:
        if el in dct.keys():
            dct[el] += 1

    # Return the futures list ordered by each value
    dic_list = [(el[0], el[1]) for el in dct.items()]
    result = sorted(dic_list, reverse=True, key=lambda x: x[1])
    return result

if __name__ =='__main__':
    target = ['青年', '合作', '工作', '中日', '开放', '消费', '经济', '推动', '双方', '巡视', '上证50', '燃料油']
    print(futures_count(target))