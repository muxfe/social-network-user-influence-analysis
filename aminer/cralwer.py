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
    errortime = 0
    count = 1
    while (start < limit):
        curapi = api + str(start) + '/' + str(offset)
        print 'fetch ' + curapi
        try:
            response = urllib2.urlopen(urllib2.Request(curapi))
            data = response.read()
            fwriter.write(data + "\n")
            start = start + offset + 1
            print str(count) + ' ok!'
        except:
            print str(count) + ' error!'
            errortime += 1
            if errortime > 3:
                start = start + offset + 1
        time.sleep(sleeptime)
        count += 1
    fwriter.close()
    return

def fetchPub(sleeptime = 3, pass = 0):
    freader = open('user.json', 'r')
    fwriter = open('publication.json', 'w')
    count = 0
    for raw_data in freader:
        json_array = json.loads(raw_data)
        for user in json_array:
            count += 1
            if count <= pass:
                print 'pass ' + str(count)
                continue
            uid = user['id']
            n_pubs = user['n_pubs']
            api = 'https://api.aminer.org/api/person/pubs/' + str(uid) +'/all/year/0/' + str(n_pubs)
            print 'fetch ' + api
            try:
                response = urllib2.urlopen(urllib2.Request(api))
                data = response.read()
                fwriter.write(data + "\n")
                print str(count) + ' ok!'
            except:
                print str(count) + ' error!'
            time.sleep(sleeptime)
    freader.close()
    fwriter.close()
    return

if __name__ == '__main__':
    # fetchUser(limit = 10000)
    fetchPub()
    print 'Done!'
