#!/home/knielbo/virtenvs/nuke/bin/python
"""
Simple data loader class with preprocessor option
Input:
    - preprocessors: list of preprocessors
    - jsonPath: str with path to reddit json object
    - tags: list of tags to extract
"""
import os
import json
from pandas import DataFrame

class DatasetLoader:
    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors

        if self.preprocessors is None:
            self.preprocessors = list()

    def load(self, jsonPath, tags, verbose=-1):
        data = list()
        with open(jsonPath, "r") as f:
            lignes = f.readlines()
            for i, ligne in enumerate(lignes):# i for verbose
                jsonObject = json.loads(ligne)
                datum = list()
                for tag in tags:
                    content = jsonObject[tag]
                    if self.preprocessors is not None:
                        for p in self.preprocessors:
                            if tag in p.tag:
                                content = p.preprocess(content)

                    datum.append(content)
                data.append(datum)

                if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                    print("[INFO] processed {}/{}".format(i+1, len(lignes)))
        
        
        data = DataFrame(data)
        data.columns = tags
        
        return data
