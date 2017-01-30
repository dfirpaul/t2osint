#!/usr/bin/env python

import urllib2
import re

def writeYAML():
    yamlFile = open('bambenekconsultingc2dns.csv','w')
    url='http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt'
    html = urllib2.urlopen(url)
    yamlFile.write('domain,info,reference'+"\n")
    for line in html.readlines():
        line = re.sub('\\r|\\n', '', line)
        for match in re.finditer(r"(?m)^([^,#]+),Domain used by ([^,/]+)", line):
            yamlFile.write('{0}bambenekconsulting.com\n'.format("{0:s},{1:s}(malware),".format(match.group(1), match.group(2).strip())))
    yamlFile.close()

if __name__=="__main__":
    writeYAML()