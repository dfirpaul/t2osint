import urllib2, re

def writeYAML():
    yamlFile = open('alienvault.csv','w')
    url='http://reputation.alienvault.com/reputation.generic'
    html = urllib2.urlopen(url)
    yamlFile.write('dest_ip,info,reference'+"\n")
    for line in html.readlines():
        #line = re.sub('\\r|\\n','',line)
        line = line.strip()
        if not line or line.startswith('#') or '.' not in line:
            continue
        if " # " in line:
            reason = line.split(" # ")[1].split()[0].lower()
            if reason == "scanning":
                continue
            yamlFile.write(line.split(" # ")[0] + ',bad reputation' + ',alienvault.com\n')
        #yamlFile.write(line+",zeus (malware)"+",abuse.ch"+"\n")
    yamlFile.close()

if __name__=="__main__":
    writeYAML()