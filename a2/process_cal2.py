#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 01 08:35:33 2022
@author: rivera

This is a text processor that allows to translate XML-based events to YAML-based events.
CAREFUL: You ARE NOT allowed using (i.e., import) modules/libraries/packages to parse XML or YAML
(e.g., yaml or xml modules). You will need to rely on Python collections to achieve the reading of XML files and the
generation of YAML files.
"""
from email.errors import StartBoundaryNotFoundDefect
import sys
import re
import time
import datetime
from tracemalloc import start

'''
Function: main
    Description: represents the entry point of the program.
    Inputs: 
        - argc: indicates the number of arguments to be passed to the program.
        - argv: an array of strings containing the arguments passed to the program.
    Output: an integer describing the result of the execution of the program:
        - 0: Successful execution.
        - 1: Erroneous execution.
'''


def main():
    """The main entry point for the program.
    """
    # Calling a dummy function to illustrate the process in Python
    # print('Hi! from:', sys.argv[0])

    if len(sys.argv) < 6:
        sys.exit(1)

    start_date = remove_arguments_beginning(sys.argv[1])
    start_date = time.strptime(start_date, "%Y/%m/%d")
    end_date = remove_arguments_beginning(sys.argv[2])
    end_date = time.strptime(end_date, "%Y/%m/%d")
    event_file = remove_arguments_beginning(sys.argv[3])
    circuit_file = remove_arguments_beginning(sys.argv[4])
    broadcasters_file = remove_arguments_beginning(sys.argv[5])

    list_of_events = parse_events(event_file)
    list_of_circuits = parse_events(circuit_file)
    list_of_broadcasters = parse_events(broadcasters_file)

    list_of_events = get_broadcasters(list_of_events, list_of_broadcasters)
    list_of_events = get_circuits(list_of_events, list_of_circuits)

    writen_file = open_output_file()

    events_on_date(start_date, end_date, writen_file, list_of_events)

    writen_file.close()

    sys.exit(0)


'''
    Function: remove_arguments_beginning
    Description: takes a string in the form of "--<tag>=<info>" and removes the "--<tag>"
    Inputs:
        - argument: a string in the form of "--<tag>=<info>"
    Output:
        - string "<info>"
'''


def remove_arguments_beginning(argument):
    return re.sub(r'^.*?=', '', argument)


'''
    Function: parse_events
    Description: takes an xml file and parses information into a list of dictionary
    Input: 
        - file: xml file to be parsed
    Output:
        - list of dictionaries
'''


def parse_events(file):
    list_of_events = []
    f = open(file, 'r')
    f.readline()
    line = f.readline()
    line = f.readline()
    while line != '':
        dictionary_of_events = {}
        while line.startswith("    </") == False:
            line = line.strip()
            tag = get_tag(line)
            line = get_line(line)
            if tag == 'broadcaster':
                line = line.split(',')
            dictionary_of_events[tag] = line
            line = f.readline()
        list_of_events.append(dictionary_of_events)
        line = f.readline()
        line = f.readline()
    f.close()
    return list_of_events


'''
    Function: get_tag
    Description: takes a line of an xml file in the form of '<tag> Description <tag>" and gets the tag
    Input: 
        - line: a string in the form of "<tag> Description <tag>"
    Output: 
        - the tag
'''


def get_tag(line):
    # https://www.pythonforbeginners.com/basics/how-to-split-a-string-between-characters-in-python
    start = line.index('<')
    end = line.index('>', start+1)
    tag = line[start+1:end]
    return tag


'''
    Function: get_line
    Description: takes a line of an xml file in the form of '<tag> Description <tag>" and gets the description
    Input: 
        - line: a string in the form of "<tag> Description <tag>"
    Output: 
        - the description
'''


def get_line(line):
    return re.sub(r'<.+?>', '', line)


'''
    Function: open_output_file
    Description: opens a file to be written called output.yaml
    Input: 
        - None
    Output: 
        - the output file
'''


def open_output_file():
    file = open("output.yaml", "w")
    file.write("events:")
    return file


'''
    Function: get_dates
    Description: takes a list of events and gets all of the events on a given date
    Input: 
        - list_of_events: list of dictionary events
        - start_date: date of events to be found
    Output: 
        - list of events on the given date
'''


def get_dates(list_of_events, start_date):
    events_on_day = []
    for event in list_of_events:
        event_date = datetime.date(int(event["year"]), int(
            event["month"]), int(event["day"]))
        if event_date == start_date:
            events_on_day.append(event)
    return events_on_day


'''
    Function: eventOnDate
    Description: iterates dates between start_date and end_date. 
    Gets a list of the events on each day between the start and end dates
    Calls functions to write the events to the given output file
    Input: 
        - start_date: the first date
        - end_date: the last date
        - writen_file: the file to be written
        - list_of_events: a list of dictionary events
    Output:
        - None
'''


def events_on_date(start_date, end_date, writen_file, list_of_events):
    start_date_comparison = datetime.date(
        start_date.tm_year, start_date.tm_mon, start_date.tm_mday)
    end_date_comparison = datetime.date(
        end_date.tm_year, end_date.tm_mon, end_date.tm_mday)
    delta = datetime.timedelta(days=1)

    while start_date_comparison <= end_date_comparison:
        events_on_date = get_dates(list_of_events, start_date_comparison)
        if events_on_date:
            write_date(start_date_comparison, writen_file)
            events_on_date = sort_dates(events_on_date)
            events_on_date = twelve_hour_time(events_on_date)
            write_events(events_on_date, writen_file, start_date_comparison)
        start_date_comparison += delta


'''
    Function: write_date
    Description: writes a date in the form of "DD-MM-YYYY" to the given file 
    Input: 
        - start_date: date to be written
        - writen_file: file to write the date
    Output: 
        -  None
'''


def write_date(start_date, writen_file):

    day = start_date.day
    month = start_date.month
    year = start_date.year
    start_date = datetime.datetime(year, month, day)

    day = start_date.strftime("%d-%m-%Y:")

    writen_file.write("\n  - " + day)


'''
    Function: sort_dates
    Description: sorts a list of dictionary events and sorts them by their start times
    Input: 
        - events: a list of dictionary events that occur all on the same day
    Output: 
        - returns the list of sorted events
'''


def sort_dates(events):

    for i in range(len(events)):
        smallest = i
        for p in range(i, len(events)):
            event_time = events[p]['start']
            event_time = time.strptime(event_time, "%H:%M")
            smallest_time = events[smallest]['start']
            smallest_time = time.strptime(smallest_time, "%H:%M")

            if event_time < smallest_time:
                smallest = p
        a = events[i]
        b = events[smallest]

        events[i] = b
        events[smallest] = a
    return events


'''
    Function: twelve_hour_time
    Description: takes a list of dictionary events and changes the start and end time to 12h clock
    Input: 
        - events: list of dictionary events
    Output: 
        - list of events in twelve hour time
'''


def twelve_hour_time(events):
    for event in events:
        time_start = event['start']
        time_start = time.strptime(time_start, "%H:%M")
        time_start = time.strftime("%I:%M %p", time_start)
        event['start'] = time_start

        time_end = event['end']
        time_end = time.strptime(time_end, "%H:%M")
        time_end = time.strftime("%I:%M %p", time_end)
        event['end'] = time_end
    return events


'''
    Function: get_broadcasters
    Description: gets the broadcasters associated with an event
    Input: 
        - events: list of dictionary events
        - broadcasters: list of dictionary broadcasters
    Output: 
        - a list of events with the broadcasters
'''


def get_broadcasters(events, broadcasters):
    for event in events:
        for i in range(len(event['broadcaster'])):
            for b in broadcasters:
                if b['id'] == event['broadcaster'][i]:
                    event['broadcaster'][i] = b['name']

    return events


'''
    Function: get_circuits
    Description: gets the circuits associated with an event
    Input: 
        - events: list of dictionary events
        - broadcasters: list of dictionary circuits
    Output: 
        - a list of events with the circuits
'''


def get_circuits(events, circuits):
    for event in events:
        for c in circuits:
            if c['id'] == event['location']:
                circuit = {
                    'name': c['name'], 'direction': c['direction'], 'location': c['location'], 'timezone': c['timezone']}
                event['location'] = circuit

    return events


'''
    Function: write_events
    Description: writes the events to a file
    Input: 
        - events: list of dictionary events
        - writen_file: the file to written
        - start_date: the date on which the events occur
    Output: 
        - None
'''


def write_events(events, writen_file, start_date):
    for event in events:
        writen_file.write("\n    - id: " + event['id'])
        writen_file.write("\n      description: " + event['description'])
        writen_file.write(
            "\n      circuit: " + event['location']['name'] + " (" + event['location']['direction'] + ")")
        writen_file.write("\n      location: " + event['location']['location'])
        writen_file.write(
            "\n      when: " + event['start'] + " - " + event['end'] + " " + start_date.strftime("%A, %B %d, %Y") + " (" + event['location']['timezone'] + ")")
        writen_file.write("\n      broadcasters:")
        for broadcast in event['broadcaster']:
            writen_file.write("\n        - " + broadcast)


if __name__ == '__main__':
    main()
