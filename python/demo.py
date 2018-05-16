#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
# from gensim import models, corpora, similarities
# import jieba
# import pandas as pd
# import numpy as np

from shangwubu.execute_scrapy import small_test
from data_io import read, read_dir
from news_df import news_df
from plsa_model import plsa_model
from new_news_topic import new_news_topic
from futures_count import futures_count


def run_test():

    small_test()
    path = os.path.dirname(__file__) + r'/shangwubu/small_result.csv'

    df = read(path)
    df = news_df(df)

    lsi = plsa_model(df)

    new_news = u'2018年4月19日，商务部发布2018年第39号公告，公布对原产于美国、欧盟和新加坡的进口卤化丁基橡胶（也称卤代丁基橡胶）反倾销调查的初裁裁定。商务部初步裁定原产于美国、欧盟和新加坡的进口卤化丁基橡胶存在倾销，国内卤化丁基橡胶产业受到了实质损害，且倾销与实质损害之间存在因果关系，并决定对原产于美国、欧盟和新加坡的进口卤化丁基橡胶产品实施保证金形式的临时反倾销措施。根据裁定，自2018年4月20日起，进口经营者在进口原产于美国、欧盟和新加坡的卤化丁基橡胶时，应依据裁定所确定的各公司倾销幅度（26.0%-66.5%）向中华人民共和国海关提供相应的保证金。应国内卤化丁基橡胶产业申请，商务部于2017年8月30日发布公告，决定对原产于美国、欧盟和新加坡的进口卤化丁基橡胶进行反倾销立案调查。该产品归在《中华人民共和国进出口税则》：40023910和40023990税号项下。'
    lst = new_news_topic(lsi, new_news)
    print(lst)

    counts = futures_count(lst)
    print(counts)

if __name__ == '__main__':
    run_test()
