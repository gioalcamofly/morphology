from __future__ import division
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def efficiency(tags):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = open('tags.txt')
    line = f.readline()
    bad_tags = {}
    count = 0
    index = 0
    for item in tags.values():
        if line.strip() == item[1]:
            count += 1
        else:
            print item[0], line.strip() + ' ' + item[1]
            index += 1
        line = f.readline()
    print index
    return (count/662)*100



