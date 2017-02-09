###############################################################################
# Author: Abhimanyu Banerjee
# Date Created: 1/30/2017
# 
# File Description: This script downloads the videos corresponding to each clip
# listed on the 'klipd.com' website
###############################################################################

from __future__ import print_function
from os.path import isfile, isdir, join
from multiprocessing import Pool
import json
import pdb
import os

klipd_vid_repo_path = join("..", "data", "clips")

'''downloads the media associated with the url passed as parameter'''
def downloadVideo(item):
    #pdb.set_trace()
    idx = item[0]
    video_url = item[1]["vid_url"]
    os.system("wget -O " + join(klipd_vid_repo_path, "clip_" + str(idx) + ".mp4 ") + video_url)

if __name__ == '__main__':
    
    pool = Pool(16)

    #relevant path names and urls
    video_json_path = join("..", "data", "vids_urls.json")
    
    #check if data store for clip video urls exist
    if isfile(video_json_path):
        with open(video_json_path, "r") as f:
            video_dict = json.load(f)

            #check if the required repo directory for the videos exists
            if not isdir(klipd_vid_repo_path):
                os.mkdir(klipd_vid_repo_path)
                #os.mkdir(join(klipd_vid_repo, "clips"))

            '''for item in video_dict["success"].items():
                downloadVideo(item, klipd_vid_repo_path)'''
            pool.map(downloadVideo, video_dict["success"].items())
            