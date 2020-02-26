"""

"""
import re

class RegxFilter:
    def __init__(self, tag, pattern):
        self.tag = tag
        self.pattern = re.compile(r"{}".format(pattern),flags=re.MULTILINE)
    
    def preprocess(self, text):
        return self.pattern.sub(" ", text)

        