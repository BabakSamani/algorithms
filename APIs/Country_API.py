# Complete the function below.
import sys
import os
import urllib2
import json


def get_countries(s, p):
    count = 0
    url = 'https://jsonmock.hackerrank.com/api/countries/search?name=' + s + '&page=1'
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    result = json.loads(res.read())
    print(result['total_pages'])
    for i in range(0, len(result['data'])):
        r = result['data'][i]
        pop = r['population']
        if int(pop) > p:
            count += 1
    return count


# f = open(os.environ['OUTPUT_PATH'], 'w')
#
# try:
#     _s = raw_input()
# except:
#     _s = None
#
# _p = int(raw_input())
#
# res = getCountries(_s, _p)
# f.write(str(res) + "\n")
#
# f.close()

print(get_countries('in', 1000000))
