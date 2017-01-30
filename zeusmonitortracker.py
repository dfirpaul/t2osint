#!/usr/bin/env python

import urllib2, re


def writeYAML():
    # yamlFile = open('zeustrackermonitor.csv','w')
    gotit = {}
    url = 'http://zeustracker.abuse.ch/monitor.php?filter=all'
    html = urllib2.urlopen(url)
    # yamlFile.write('dns,info,reference'+"\n")
    for line in html.readlines():
        for match in re.finditer(r'<td>([^<]+)</td><td><a href="/monitor.php\?host=([^"]+)', line):
             gotit[match.group(2)] = (match.group(1).lower() + " (malware)" )
    "".join(gotit)
        #
        # line = re.sub('\\r|\\n','',line)
        #   line = line.strip()
        #  if not line or line.startswith('#'):
        #     continue
        #  yamlFile.write(line+",zeus (malware)"+",abuse.ch"+"\n")
        # yamlFile.close()


if __name__ == "__main__":
    writeYAML()
