'''
@Descripttion: 
@Author: Defu Li
@Date: 2019-10-24 21:59:03
'''
from drqa import pipeline
from drqa.retriever import DEFAULTS
import drqa.tokenizers
import logging


class SeaWiki(object):
    def __init__(self, wiki_path, tfidf_path):

        DEFAULTS['db_path'] = wiki_path
        DEFAULTS['tfidf_path'] = tfidf_path
        
        # 输出日志
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s: [ %(message)s ]', '%m/%d/%Y %I:%M:%S %p')
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        logger.addHandler(console)

        self.qa = pipeline.DrQA()



    def search(self, question, top_docs=5, is_title=True, is_document=True):
        title, document= self.qa.process(question, n_docs=top_docs)

        if is_title and is_document:
            return title, document
        elif is_title and (not is_document):
            return title
        elif (not is_title) and is_document:
            return document

