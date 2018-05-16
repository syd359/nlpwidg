from gensim import models, corpora, similarities
from gensim.models import word2vec
from gensim.summarization import keywords
import jieba
import logging
import os

from extract_key_words import extract_key_words
from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

def new_news_topic(lsi, new_doc):
    '''
    Given
    :param lsi:
    :param new_doc:
    :return:
    '''
    logger.info('Analysing the new document topics')

    # new_doc = '2018年4月19日，商务部发布2018年第39号公告，公布对原产于美国、欧盟和新加坡的进口卤化丁基橡胶（也称卤代丁基橡胶）反倾销调查的初裁裁定。商务部初步裁定原产于美国、欧盟和新加坡的进口卤化丁基橡胶存在倾销，国内卤化丁基橡胶产业受到了实质损害，且倾销与实质损害之间存在因果关系，并决定对原产于美国、欧盟和新加坡的进口卤化丁基橡胶产品实施保证金形式的临时反倾销措施。根据裁定，自2018年4月20日起，进口经营者在进口原产于美国、欧盟和新加坡的卤化丁基橡胶时，应依据裁定所确定的各公司倾销幅度（26.0%-66.5%）向中华人民共和国海关提供相应的保证金。应国内卤化丁基橡胶产业申请，商务部于2017年8月30日发布公告，决定对原产于美国、欧盟和新加坡的进口卤化丁基橡胶进行反倾销立案调查。该产品归在《中华人民共和国进出口税则》：40023910和40023990税号项下。'

    # The stop words are not in the stopwords.txt
    stop_words = [u'，', u'。', u'、', u'（', u'）', u'·', u'！', u' ', u'：', u'“', u'”', u'\n', u'\r', u'\u3000', u'\xa0',
                  u'；', u'-', u'—', u'\t']
    path = os.path.dirname(__file__) + r'\..' + r'\data\stopwords.txt'
    stopwords = stopwordlist(path)

    seg = jieba.cut(new_doc)
    new_doc_list = [i for i in seg if i not in stop_words and i not in stopwords]

    dictionary = corpora.Dictionary.load('data.dict')
    bow = dictionary.doc2bow(new_doc_list)
    new_doc_dist = lsi[bow]  # (#topic , topic value)

    # get the top topic id and its value
    top_topic = sorted(new_doc_dist, reverse=True, key=lambda x: abs(x[1]))[0]
    topic = lsi.print_topic(top_topic[0])
    # topic_id = top_topic[0]
    return extract_key_words(topic)



def stopwordlist(filepath):
    stopwords = [line.strip() for line in open(filepath, encoding='utf-8').readlines()]
    return stopwords
