#!/usr/bin/env python

import sys

finput = sys.stdin
neg_max = 50000
pos_max = 50000


def count_category(finput):
    neg_count =0
    pos_count = 0
    for line in finput:

        line = line.strip()
        line_data = line.split(",")
        category = line_data[0]

        if (int(category) == 0):
            neg_count += 1
        elif (int(category) == 1):
            pos_count += 1
    print pos_count
    print neg_count


def make_file(neg_max, pos_max):
    neg_count =0
    pos_count = 0
    for line in finput:
        line = line.strip()
        line_data = line.split(",")
        category = line_data[1]
        if(category == "Sentiment"):
            continue

        if(neg_count >= neg_max & pos_count >= pos_max):
            break

        if (int(category) == 0):
            if(neg_count < neg_max):
                neg_count += 1
                print line
            else:
                continue
        elif (int(category) == 1):
            if(pos_count < pos_max):
                pos_count += 1
                print line
            else:
                continue


make_file(neg_max, pos_max)
#count_category(finput)