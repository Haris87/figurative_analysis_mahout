#!/usr/bin/env python


from TweetUtils.models.Config import Config
from TweetUtils.tweet_utils import TweetUtils
import sys
import json

# "OH_SO": "Looks for Oh, so * pattern e.g. ",
# "DONT_YOU": "Looks for Don*t you * pattern e.g. ",
# "AS_GROUND_AS_VEHICLE": "Looks for as * as * pattern e.g.:",
# "CAPITAL": "Presence of CAPITALIZED words -- indicates heightened emotion ",
# "HT" : "",
# "HT_POS": "",
# "HT_NEG": "",
# "LINK": "Presence/Absence of ulrs",
# "POS_SMILEY": "",
# "NEG_SMILEY": "",
# "NEGATION": "Presense/Absense of negations e.g. I love working at weekends#NOT or I don't love working at weekends.",
# "REFERENCE": "@user",
# "questionmark": "Presense/Absense of ?",
# "exclamation": "Presense/Absense of !",
# "fullstop": "Presense/Absense of .",
# "RT": "Presense/Absense of RT",
# "LAUGH": "Presense/Absense of laugh patterns",
# "LOVE": "Presense/Absense of <3",
# "res": "Calculate Resnik Text Similarity Measure. [0,1]",
# "lin": "Calculate Lin Text Similarity Measure.",
# "wup": "Calculate Wup Text Similarity Measure.",
# "path": "Calculate Path Text Similarity Measure.",
# "postags": "POS-Tag tweet.",
# "swn_score": "Calculate total SentiWordNet Score for Tweet",
# "s_word": "SentiWordNet score for each word, e.g. s_word-{index of word in tweet} s_word-1 : 1.2",
# "contains_": "contains_{word}: True/False",

# function to convert dictionary of features to csv string
def dict_to_csv(dictionary):
    csv = ''
    csv += str(dictionary["OH_SO"])+"," if dictionary.has_key("OH_SO") else ","
    csv += str(dictionary["DONT_YOU"])+"," if dictionary.has_key("DONT_YOU") else ","
    csv += str(dictionary["AS_GROUND_AS_VEHICLE"])+"," if dictionary.has_key("AS_GROUND_AS_VEHICLE") else ","
    csv += str(dictionary["CAPITAL"])+"," if dictionary.has_key("CAPITAL") else ","
    csv += str(dictionary["HT"])+"," if dictionary.has_key("HT") else ","
    csv += str(dictionary["HT_POS"])+"," if dictionary.has_key("HT_POS") else ","
    csv += str(dictionary["HT_NEG"])+"," if dictionary.has_key("HT_NEG") else ","
    csv += str(dictionary["LINK"])+"," if dictionary.has_key("LINK") else ","
    csv += str(dictionary["POS_SMILEY"])+"," if dictionary.has_key("POS_SMILEY") else ","
    csv += str(dictionary["NEG_SMILEY"])+"," if dictionary.has_key("NEG_SMILEY") else ","
    csv += str(dictionary["NEGATION"])+"," if dictionary.has_key("NEGATION") else ","
    csv += str(dictionary["REFERENCE"])+"," if dictionary.has_key("REFERENCE") else ","
    csv += str(dictionary["questionmark"])+"," if dictionary.has_key("questionmark") else ","
    csv += str(dictionary["exclamation"])+"," if dictionary.has_key("exclamation") else ","
    csv += str(dictionary["fullstop"])+"," if dictionary.has_key("fullstop") else ","
    csv += str(dictionary["RT"])+"," if dictionary.has_key("RT") else ","
    csv += str(dictionary["LAUGH"])+"," if dictionary.has_key("LAUGH") else ","
    csv += str(dictionary["LOVE"])+"," if dictionary.has_key("LOVE") else ","
    csv += str(dictionary["res"])+"," if dictionary.has_key("res") else ","
    csv += str(dictionary["lin"])+"," if dictionary.has_key("lin") else ","
    csv += str(dictionary["wup"])+"," if dictionary.has_key("wup") else ","
    csv += str(dictionary["path"])+"," if dictionary.has_key("path") else ","
    csv += str(dictionary["postags"])+"," if dictionary.has_key("postags") else ","
    csv += str(dictionary["swn_score"])+"," if dictionary.has_key("swn_score") else ","
    csv += str(dictionary["s_word"])+"," if dictionary.has_key("s_word") else ","
    csv += str(dictionary["contains_"])+"," if dictionary.has_key("contains_") else ","
    return csv


#MAIN
utils = TweetUtils(Config(True, True))

# input comes from STDIN (standard input)
finput = sys.stdin

# test input
# finput = ['1,1,0,this is an awesome tweet!', '2,0,0,i dont like this stuff...']

for line in finput: #sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    line_data = line.split("\t")
    line_data = line_data[1].split(",")
    category = line_data[1]
    line = line_data[3]

    # remove "," for csv format
    line = line.replace(",","")

    tweet = utils.process(line)

    # convert features to csv
    csv_features = dict_to_csv(tweet.feature_dict)

    output_value = str(tweet) + ',' + csv_features
    print '%s,%s' % (category, output_value)