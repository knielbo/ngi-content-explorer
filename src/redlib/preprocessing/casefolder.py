"""
Simple preprocesser for casefolding
"""
class CaseFolder:
    def __init__(self, tag, lower=True):
        self.lower = lower
        self.tag = tag
    
    def preprocess(self, text):
        if self.lower:
            return text.lower()
        else:
            return text.upper()