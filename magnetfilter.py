#!/usr/bin/python
import sys
import urllib
import requests

TRACKERS_URL = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt"
TRACKERS_URL2 = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt"
trackers = []
for line in requests.get(TRACKERS_URL, stream=True).iter_lines():
    if line: trackers.append(urllib.quote(line))
for line in requests.get(TRACKERS_URL2, stream=True).iter_lines():
    if line: trackers.append(urllib.quote(line))
tracker_addition = "&tr=".join(trackers)

def unquote(str):
    if str[0] == "\"" and str[len(str) - 1] == "\"":
        return str.substring(1,len(str) - 1)
    return str

def filter_magnet_link(link):
    link = unquote(link)
    link = link.replace("zer0day.ch", "tracker.zer0day.to")
    return link + "&tr=" + tracker_addition

print ''
for link in sys.argv:
    if link == sys.argv[0]:
        continue
    else:
        print filter_magnet_link(link)
print ''
