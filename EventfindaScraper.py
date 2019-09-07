import csv
import xml.sax
import os
import httplib2

rows = [["Title", "Description", "Where", "Time", "Icon"]]

class EventHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.description = ""
        self.where = ""
        self.time = ""
        self.icon_url = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "enclosure":
            url = attributes['url']
            self.icon_url = url

    def endElement(self, tag):
        if tag == "item":
            rows.append([self.title, self.description, self.where, self.time, self.icon_url])
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "description":
            self.description = content.split(" ...")[0] + "..."
        elif self.CurrentData == "content":
            self.time = content[:-(len(content) - (len(content.split(', ')[len(content.split(', '))-1]) + (len(content.split(', ') * 2))))]
            self.where = content.split(", ")[len(content.split(', '))-1]



if ( __name__ == "__main__"):
    content = open('eventfinda.xml', 'r')
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(EventHandler())
    parser.parse(content)

    with open("export/eventfinda.csv", "wb") as eventCsv:
        writer = csv.writer(eventCsv)
        writer.writerows(rows)
        eventCsv.close()