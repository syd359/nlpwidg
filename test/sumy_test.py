def sumy_test():
    import sumy
    from sumy.summarizers import lsa
    import jieba
    import logging

    # import dataframe
    df = news_df()
    texts = df['content'].tolist()

    from sumy.summarizers.lsa import LsaSummarizer
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer, ChineseWordTokenizer

    string = df.content[2]
    parser = PlaintextParser.from_string(string, Tokenizer('chinese'))
    summarizer_2 = LsaSummarizer()
    summary_2 = summarizer_2(parser.document, 10)

    print(string)
    print("-------------------------------------")
    for sentence in summary_2:
        print(sentence)

    return

sumy_test()