#!/usr/bin/python
# coding: utf-8
# crawling aminer.org data

__author__ = "x-web"

import sys
import urllib2
import json
import time


def fetchUser(start = 0, offset = 99, limit = 100, sleeptime = 3):
    fwriter = open('user.json', 'w')
    api = 'https://api.aminer.org/api/rank/person/h_index/'
    while (start < limit):
        curapi = api + str(start) + '/' + str(offset)
        print 'fetch ' + curapi
        response = urllib2.urlopen(urllib2.Request(curapi))
        data = response.read()
        fwriter.write(data + "\n")
        start = start + offset + 1
        time.sleep(sleeptime)
    fwriter.close()
    return

def fetchPub(uid, start = 0, offset = 99, limit = 100, sleeptime = 3):
    fwriter = open('publication.json', 'w')
    api = 'https://api.aminer.org/api/person/pubs/' + uid +'/all/year/'
    while (start < limit):
        curapi = api + str(start) + '/' + str(offset)
        print 'fetch ' + curapi
        response = urllib2.urlopen(urllib2.Request(curapi))
        data = response.read()
        fwriter.write(data + "\n")
        start = start + offset + 1
        time.sleep(sleeptime)
    fwriter.close()
    return

if __name__ == '__main__':
    fetchUser(limit = 10000)
    print 'Done!'
