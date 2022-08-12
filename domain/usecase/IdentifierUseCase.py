from datetime import date, timedelta

import self as self
from sqlalchemy import null
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import googletrans
from googletrans import Translator
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import infrastructure.adapter.NewsBeautifulSoupAdapter as bs
import pandas as pd
import infrastructure.adapter.NewsDatabaseAdapter as ndba


class IdentifierUseCase:

    def __init__(self):
        self.news_db_adapter = ndba.NewsDatabaseAdapter()
        self.facebook_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.translator = Translator(service_urls=['translate.googleapis.com'])
        self.roberta_classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")
        # self.roberta_classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")
        self.news_db_adapter = ndba.NewsDatabaseAdapter()

        self.stop_words = set(stopwords.words('english'))

        self.candidate_labels = ['travel', 'politics', 'sports', 'war', 'nature', 'health', 'elections',
                                 'economy', 'entertainment', 'education', 'violence', 'fashion', 'technology', 'arts',
                                 'music',
                                 'justice', 'food', 'business', 'styles', 'science']


    # def identifify_facebook_model(self):
    #     news = self.news_db_adapter.get_stored_news_for_prediction()
    #     print(news)
    #     translated_news = self.translator.translate(new, src='pt').text
    #     word_tokens = word_tokenize(translated_news)
    #     filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
    #     final_string = ''
    #     for x in filtered_sentence:
    #         final_string += ' ' + x
    #     news_classified = self.facebook_classifier(final_string, self.candidate_labels, multi_label=True)
    #     print(news_classified["sequence"])
    #     print(new)
    #     print(news_classified["labels"])
    #     print(news_classified["scores"])
    #
    #     # score = int(news_classified["scores"][0] * 100)
    #     # if score >= 80:
    #     #     return news_classified["labels"][0]
    #     # else:
    #     #     return 0


    def identifify_xlm_roberta_large_model(self):
        news = self.news_db_adapter.get_stored_news_for_prediction()
        for new in news.headline:
            translated_news = self.translator.translate(new, src='pt').text
            word_tokens = word_tokenize(translated_news)
            filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
            final_string = ''
            for x in filtered_sentence:
                final_string += ' ' + x
            news_classified_roberta = self.roberta_classifier(final_string, self.candidate_labels, multi_label=True)
            news_classified_face = self.facebook_classifier(final_string, self.candidate_labels, multi_label=True)
            # print(news_classified_roberta["sequence"])
            print(new)
            print('FACE:' + news_classified_face["labels"][0])
            print('ROBERTA:' + news_classified_roberta["labels"][0])
            # print(news_classified_face["scores"])
            self.news_db_adapter.update_news(new, news_classified_roberta["labels"][0], news_classified_face["labels"][0])
            # score = int(news_classified["scores"][0] * 100)
            # if score >= 80:
            #     return news_classified["labels"][0]
            # else:
            #     return 0

