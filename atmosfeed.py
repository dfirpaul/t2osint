import urllib2, re

def writeYAML():
    #yamlFile = open('atmos.csv','w')
    url='http://cybercrime-tracker.net/ccam.php'
    html = urllib2.urlopen(url)
    #yamlFile.write('dest_ip,info,reference'+"\n")
    for line in html.readlines():
    #print line
        for match in re.finditer(r">([^<]+\.[a-zA-Z]+)</td>\s*<td style=\"background-color: rgb\(11, 11, 11\);\"><a href=\"ccamdetail\.php\?hash=",line):
            print match.group()
        #yamlFile.write(line.split(" # ")[0] + ',bad reputation' + ',alienvault.com\n')
        #yamlFile.write(line+",zeus (malware)"+",abuse.ch"+"\n")
    #yamlFile.close()

if __name__=="__main__":
    writeYAML()