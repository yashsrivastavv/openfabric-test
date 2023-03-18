import os
import string
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
import io
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wolframalpha
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)

############################################################
# Callback function called on update config
############################################################
with open('data.txt', 'r', encoding='utf8', errors='ignore') as bank:
    process = bank.read().lower()

sentence_token = nltk.sent_tokenize(process)
word_token = nltk.word_tokenize(process)
app_id = 'GE8LH7-AKV354X7PE'
client = wolframalpha.Client(app_id)


def config(configuration: ConfigClass):
    pass


lem = WordNetLemmatizer()


############################################################
# Callback function called on each execution pass
############################################################
def Lemmatizer_token(tokens):
    return [lem.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LNormalize(text):
    return Lemmatizer_token(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    global ans
    output = []
    ques = ''
    for text in request.text:
        k = text.lower()
        ques += k
    if 'what' in ques or 'solve' in ques:
        res = client.query(ques)
        ans = next(res.results).text
    try:
        print(ans)
    except StopIteration:
        nlp_model(ques)
    nlp_model(ques)
    output.append(ans)
    return SimpleText(dict(text=output))


def nlp_model(ques):
    bot_resp = ''
    sentence_token.append(ques)
    Tfidfvec = TfidfVectorizer(tokenizer=LNormalize, stop_words='english')
    tfidf = Tfidfvec.fit_transform(sentence_token)
    values = cosine_similarity(tfidf[-1], tfidf)
    ind = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    req = flat[-2]
    if req == 1:
        bot_resp += sentence_token[ind]
        return bot_resp
