#!/usr/bin/env python

import urllib2, re

def writeYAML():
    yamlFile = open('badip.csv','w')
    url='https://www.badips.com/get/list/any/2?age=7d'
    html = urllib2.urlopen(url)
    yamlFile.write('dest_ip,info,reference'+"\n")
    for line in html.readlines():
        #line = re.sub('\\r|\\n','',line)
        line = line.strip()
        if not line or line.startswith('#') or '.' not in line:
            continue
        yamlFile.write(line+",known attacker"+",badips.com\n")
    yamlFile.close()

if __name__=="__main__":
    writeYAML()
