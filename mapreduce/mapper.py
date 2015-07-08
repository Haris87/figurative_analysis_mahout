#!/usr/bin/env python

from TweetUtils.models.Config import Config
from TweetUtils.tweet_utils import TweetUtils
import sys


#MAIN
utils = TweetUtils(Config(True, True))

# input comes from STDIN (standard input)
finput = sys.stdin

for line in finput: #sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line_data = line.split(",")
    #get id of line
    id = line_data[0]
    reducer_id = int(id) % 10
    print '%s\t%s' % (reducer_id, line)