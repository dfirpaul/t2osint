#!/usr/bin/env python

import urllib2, re

def writeYAML():
    yamlFile = open('zeustrackerdns.csv','w')
    url='http://zeustracker.abuse.ch/blocklist.php?download=domainblocklist'
    html = urllib2.urlopen(url)
    yamlFile.write('dns,info,reference'+"\n")
    for line in html.readlines():
        #line = re.sub('\\r|\\n','',line)
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        yamlFile.write(line+",zeus (malware)"+",abuse.ch"+"\n")
    yamlFile.close()

if __name__=="__main__":
    writeYAML()
