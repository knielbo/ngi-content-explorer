#!/home/knielbo/virtenvs/nuke/bin/python
"""

"""
import os
import argparse
import ast
from redlib.datasets import DatasetLoader
from redlib.preprocessing import CaseFolder
from redlib.preprocessing import UtcTime
from redlib.preprocessing import Lemmatizer
from redlib.preprocessing import RegxFilter

def main():
    # get input
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True, help="path to input json file")
    ap.add_argument("-t", "--tag", required=True, help=" list of tag(-s) to extract from subreddit")
    args = vars(ap.parse_args())
    jsonPath = args["dataset"]
    tags = ast.literal_eval(args["tag"])
    #load data
    print("[INFO] loading data...")
    le = Lemmatizer(tag="body", lang="en")
    cf = CaseFolder(tag="body", lower=True)
    ut = UtcTime(tag="created_utc")
    # remove urls
    re0 = RegxFilter(tag="body", pattern="\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*")
    # remove non alphanumeric
    re1 = RegxFilter(tag="body", pattern="\W+")
    re2 = RegxFilter(tag="body", pattern="\d")
    re3 = RegxFilter(tag="body", pattern="\s\s+")
    #dl = DatasetLoader(preprocessors=None)
    dl = DatasetLoader(preprocessors=[le, re0, cf, ut, re1, re2, re3])
    data = dl.load(jsonPath, tags, verbose=10e2)

    data.to_csv(jsonPath, index=False)
if __name__=="__main__":
    main()