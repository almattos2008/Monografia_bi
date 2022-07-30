from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import googletrans
from googletrans import Translator
import nltk

nltk.download('stopwords')

nltk.download('punkt')
facebook_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
translator = Translator(service_urls=['translate.googleapis.com'])
# classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")
roberta_classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

stop_words = set(stopwords.words('english'))

candidate_labels = ['travel', 'politics', 'sports', 'war', 'nature', 'health', 'elections',
                    'economy', 'entertainment', 'education', 'violence', 'fashion', 'technology', 'arts', 'music',
                    'justice', 'food', 'business', 'styles', 'science']


def identifify_facebook_model(news):
    translated_news = translator.translate(news, src='pt').text
    word_tokens = word_tokenize(translated_news)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    final_string = ''
    for x in filtered_sentence:
        final_string += ' ' + x
    news_classified = facebook_classifier(final_string, candidate_labels, multi_label=True)
    print(news_classified["sequence"])
    print(news)
    print(news_classified["labels"])
    print(news_classified["scores"])
    score = int(news_classified["scores"][0] * 100)
    if score >= 80:
        return news_classified["labels"][0]
    else:
        return 0

def identifify_xlm_roberta_large_model(news):
    translated_news = translator.translate(news, src='pt').text
    word_tokens = word_tokenize(translated_news)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    final_string = ''
    for x in filtered_sentence:
        final_string += ' ' + x
    news_classified = roberta_classifier(final_string, candidate_labels, multi_label=True)
    print(news_classified["sequence"])
    print(news)
    print(news_classified["labels"])
    print(news_classified["scores"])
    score = int(news_classified["scores"][0] * 100)
    if score >= 80:
        return news_classified["labels"][0]
    else:
        return 0
