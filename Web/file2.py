import urllib.request as req
import re

rep = req.urlopen('https://daum.net')
#f = open('Web/daum.html', 'wb')
#f.write(rep.read())
#f.close()

data = rep.read().decode('utf8')

result = re.findall('https://[./-_\w]+.jpg', data)
for link in result:
    idx = link.rfind('/')
    with open('Web/pic/'+link[idx+1:], 'wb') as f:
        pic = req.urlopen(link)
        f.write(pic.read())