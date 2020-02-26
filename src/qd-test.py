#!/home/knielbo/virtenvs/nuke/bin/python
"""

"""
import os
import argparse
import ast
from redlib.datasets import DatasetLoader
from redlib.preprocessing import CaseFolder
from redlib.preprocessing import UtcTime

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
    cf = CaseFolder(tag="body", lower=True)
    ut = UtcTime(tag="created_utc")
    dl = DatasetLoader(preprocessors=[cf, ut])
    data = dl.load(jsonPath, tags, verbose=10e4)
    
    print(data.head(5))
if __name__=="__main__":
    main()