from gensim import models, corpora, similarities
from gensim.models import word2vec
import jieba
import logging
import os

from news_df import news_df
from data_io import read, read_dir, read_db
from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

def plsa_model(df):
    '''
    Return the lsi model
    Corpus is the formed by the contents of the scraped announcements
    :param df:
    :return:
    '''
    #     texts = df['content'].tolist()
    texts = df['content'].tolist()

    # stopword preprocess
    stop_words = [u'，', u'。', u'、', u'（', u'）', u'·', u'！', u' ', u'：', u'“', u'”', u'\n', u'\r', u'\u3000', u'\xa0',
                  u'；', u'-', u'—', u'\t']
    path = os.path.dirname(__file__) + r'\..' + r'\data\stopwords.txt'
    stopwords = stopwordlist(path)

    # manipulate each document to a list of words
    seg_generator = [jieba.cut(text) for text in texts]
    seg_list = [[i for i in seg if i not in stop_words and i not in stopwords] for seg in seg_generator]

    logger.info('Generating the pLSA model')
    # Gensim model
    dictionary = corpora.Dictionary(seg_list)
    dictionary.save('data.dict')

    # The function doc2bow() simply counts the number of occurrences of each distinct word,
    # converts the word to its integer word id and returns the result as a sparse vector.
    corpus = [dictionary.doc2bow(seg) for seg in seg_list]
    corpora.MmCorpus.serialize('vector.mm', corpus)
    corpus = corpora.MmCorpus('vector.mm')

    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    lsi = models.lsimodel.LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=10)

    # test on the new doc

    return lsi

def stopwordlist(filepath):
    '''
    Return a list of stop words
    :param filepath:
    :return:
    '''
    stopwords = [line.strip() for line in open(filepath, encoding='utf-8').readlines()]
    return stopwords