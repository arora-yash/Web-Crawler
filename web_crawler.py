import urllib
import HTMLParser

urlText = []

#define HTML Parser
class ParseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        if(data != '\n'):
            urlText.append(data)

#create instance of HTML Parser
lParser = ParseText()

thisurl = 'http://www.yasharora.co.nf'

#feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in urlText:
    print item
