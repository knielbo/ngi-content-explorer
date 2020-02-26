"""
Simple preprocesser for utc to human readable time
"""
from datetime import datetime

class UtcTime:
    def __init__(self, tag):
        self.tag = tag
    
    def preprocess(self, s):
        return datetime.utcfromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')