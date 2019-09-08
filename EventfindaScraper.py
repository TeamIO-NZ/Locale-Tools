import csv
import json
import os

rows = [["Title", "Description", "Date", "Start Time", "End Time", "Location", "Icon"]]

if ( __name__ == "__main__"):
    file = open('events.json', 'r')
    content = json.loads(file.read())

    for e in content['events']:
        rows.append([
            e['title'], 
            e['description'], 
            e['date'], 
            e['start_time'], 
            e['end_time'], 
            e['location'], 
            e['icon']
            ])
    file.close()

    with open("export/eventfinda.csv", "wb") as eventCsv:
        writer = csv.writer(eventCsv)
        writer.writerows(rows)
        eventCsv.close()