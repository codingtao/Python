# HTMLParser

from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request

class MyHTMLParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--',data,'-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# practice

response = urllib.request.urlopen('https://www.python.org/events/python-events/')
class PythonEvent(HTMLParser):
    def __init__(self):
        super(PythonEvent,self).__init__()
        self.key = 0
        self.location_key = 0
        self.event_list = []
        self.event_tmp = []

    def handle_starttag(self, tag, attrs):
        if attrs:
            if attrs[0][1] == 'event-title' or tag == 'time':
                self.key = 1 # self.key=1 表示data需要保存
            if attrs[0][1] == 'event-location':
                self.key = 1
                self.location_key = 1 # self.location_key = 1表示单个data信息结尾

    def handle_data(self, data):
        if self.key:
            self.event_tmp.append(data)

        if self.location_key:
            self.event_list.append(self.event_tmp) # event_tmp保存进list并重置
            self.event_tmp = []

    def handle_endtag(self, tag):
        self.key = 0
        self.location_key = 0

event = PythonEvent()
event.feed(response.read().decode('utf-8'))
for i in event.event_list:
    print(i)