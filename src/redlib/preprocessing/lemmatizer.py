"""
Simple preprocesser for lemmatization
"""
import stanfordnlp

class Lemmatizer:
    def __init__(self, tag, lang="en"):
        self.tag = tag
        self.nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma',lang=lang)
    
    def preprocess(self, text):
        try:
            doc = self.nlp(text)
            lemma = [word.lemma for sent in doc.sentences for word in sent.words if word.lemma is not None]
        except:
            lemma = "nan"

        return " ".join(lemma)
        