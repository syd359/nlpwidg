import re
import os

from get_logger import get_logger

logger = get_logger(os.path.basename(__file__))

'''
Extract the key words from the given topic list
Sort the key words by value the coef in descending order 
'''

def extract_key_words(topic):
    #     new_doc_dist = lsi[bow] # (#topic , topic value)
    # s = '0.307*"原产" + 0.273*"裁定" + 0.228*"调查" + 0.207*"进口" + 0.203*"胺" + 0.203*"硝基苯" + 0.163*"邻氯" + 0.147*"高粱" + 0.138*"实质" + 0.138*"损害"'
    pattern1 = r'\"(.*?)\"'
    pattern2 = r'(\d\.\d*)\*'
    key = re.findall(pattern1, topic)
    value = re.findall(pattern2, topic)
    items = list(zip(key, value))
    sorted(items, reverse=True, key=lambda x: x[1])
    res = [x[0] for x in items]
    return res


if __name__ == '__main__':
    topic = '0.307*"原产" + 0.273*"裁定" + 0.228*"调查" + 0.207*"进口" + 0.203*"胺" + 0.203*"硝基苯" + 0.163*"邻氯" + 0.147*"高粱" + 0.138*"实质" + 0.138*"损害"'
    lst = extract_key_words(topic)
    print(lst)