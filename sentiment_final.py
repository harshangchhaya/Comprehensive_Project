import numpy as np
import spacy
import sklearn
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from string import punctuation

def processing(text):
    raw_text = nlp(text)
    tokens = [word.lemma_ if word.lemma_ != "-PRON-" else word.lower_ for word in raw_text]
    return " ".join(word for word in tokens)

def embedding(text):
    processed_text = nlp(text)
    vector = np.array([token.vector for token in processed_text])
    return vector

nlp = spacy.load("en_core_web_lg")
text = "What's up"




