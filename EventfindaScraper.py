import csv
import xml.sax
import os
import httplib2



class EventHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.description = ""
        self.where_when = ""
        self.icon_url = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "item":
            print("===== item =====")
        elif tag == "enclosure":
            url = attributes['url']
            print("Icon:", url)
            self.icon_url

    def endElement(self, tag):
        if self.CurrentData == "title":
            print("Title:", self.title)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        elif self.CurrentData == "content":
            print("Where and When:", self.where_when)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "description":
            self.description = content.split(" ...")[0] + "..."
        elif self.CurrentData == "content":
            self.where_when = content




if ( __name__ == "__main__"):
    content = open('eventfinda.xml', 'r')
    #rss_str = u'' + content.read().decode('ascii', 'ignore')
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(EventHandler())
    parser.parse(content)

