import self as self
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import googletrans
from googletrans import Translator
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import infrastructure.adapter.NewsDatabaseAdapter as ndba

class identification:
    def __init__(self):

        self.facebook_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.translator = Translator(service_urls=['translate.googleapis.com'])
        self.roberta_classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")
        # self.roberta_classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

        self.stop_words = set(stopwords.words('english'))

        self.candidate_labels = ['travel', 'politics', 'sports', 'war', 'nature', 'health', 'elections',
                            'economy', 'entertainment', 'education', 'violence', 'fashion', 'technology', 'arts', 'music',
                            'justice', 'food', 'business', 'styles', 'science', 'weather']


    def identifify_facebook_model(self, news):
        translated_news = self.translator.translate(news, src='pt').text
        word_tokens = word_tokenize(translated_news)
        filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
        final_string = ''
        for x in filtered_sentence:
            final_string += ' ' + x
        news_classified = self.facebook_classifier(final_string, self.candidate_labels, multi_label=True)
        print(news_classified["sequence"])
        print(news)
        print(news_classified["labels"])
        print(news_classified["scores"])
        score = int(news_classified["scores"][0] * 100)
        if score >= 80:
            return news_classified["labels"][0]
        else:
            return 0

    def identifify_xlm_roberta_large_model(self, news):
        translated_news = self.translator.translate(news, src='pt').text
        word_tokens = word_tokenize(translated_news)
        filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
        final_string = ''
        for x in filtered_sentence:
            final_string += ' ' + x
        news_classified = self.roberta_classifier(final_string, self.candidate_labels, multi_label=True)
        print(news_classified["sequence"])
        print(news)
        print(news_classified["labels"])
        print(news_classified["scores"])
        score = int(news_classified["scores"][0] * 100)
        if score >= 80:
            return news_classified["labels"][0]
        else:
            return 0
