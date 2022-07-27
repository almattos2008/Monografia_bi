from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import googletrans
from googletrans import Translator
import nltk

nltk.download('stopwords')
nltk.download('punkt')
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
translator = Translator(service_urls=['translate.googleapis.com'])
# classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")
# classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

stop_words = set(stopwords.words('portuguese'))

# candidate_labels = ['viagem', 'politica', 'esporte', 'guerra', 'mundo', 'natureza', 'policial', 'saúde', 'eleições',
#                     'economia', 'televisão', 'educação', 'violência', 'moda', 'tecnologia', 'artes', 'música']

candidate_labels = ['travel', 'politics', 'sports', 'war', 'world', 'nature', 'health', 'elections',
                    'economy', 'entertainment', 'education', 'violence', 'fashion', 'tecnology', 'arts', 'music']


def identifify(news):
    word_tokens = word_tokenize(news)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    final_string = ''
    for x in filtered_sentence:
        final_string += ' ' + x
    # translated_news = translator.translate("final_string", src='pt').text
    news_classified = classifier(final_string, candidate_labels, multi_label=True)["labels"][0]
    # news_classified = classifier(filtered_sentence, candidate_labels)["labels"][0]
    return news_classified


# word_tokens = word_tokenize("news a bela e a fera")
# filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(word_tokens)
# final_string=''
# for x in filtered_sentence:
#     final_string += ' ' + x
# news_classified = classifier(final_string, candidate_labels)["labels"][0]
# print(news_classified)