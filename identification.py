from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#
# sequence_to_classify = "one day I will see the world"
# candidate_labels = ['travel', 'cooking', 'dancing']
# print(classifier(sequence_to_classify, candidate_labels))
#
# sequence_to_classify = "Holanda é o destino de muitos museólogos"
# candidate_labels = ['viagem', 'politica', 'esporte', 'guerra', 'mundo', 'natureza']
# print(classifier(sequence_to_classify, candidate_labels))
#
# sequence_to_classify = "Exclusivo: Volodymyr Zelensky critica a posição de neutralidade do presidente Bolsonaro na guerra"
# candidate_labels = ['viagem', 'politica', 'esporte', 'guerra', 'mundo', 'natureza']
# print(classifier(sequence_to_classify, candidate_labels))


# sequence_to_classify = "Onda de calor extremo atinge a Europa"
candidate_labels = ['viagem', 'politica', 'esporte', 'guerra', 'mundo', 'natureza', 'policial', 'saúde']
# print(classifier(sequence_to_classify, candidate_labels)["labels"][0])

def identifify(news):
    news_classified = classifier(news, candidate_labels)["labels"][0]
    test = classifier(news, candidate_labels)
    print(test)
    return news_classified
