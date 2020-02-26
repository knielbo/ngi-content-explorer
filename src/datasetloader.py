#!/home/knielbo/virtenvs/nuke/bin/python
"""

"""
import os
import json
from pandas import DataFrame
from datetime import datetime


class DatasetLoader():
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
                    # TODO: add preprocessor loop here
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