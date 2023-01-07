# JetBrains Academy - Core Python course
# Easy Rider Bus Company project
# https://hyperskill.org/projects/128
# Submitted by Chris Freeman - Stage 6/6 7-Jan-2023

import json
from itertools import chain


bus_schema = {'bus_id': (int, 'r'),
              'stop_id': (int, 'r'),
              'stop_name': (str, 'r'),
              'next_stop': (int, 'r'),
              'stop_type': (str, ''),
              'a_time': (str, 'r')
              }

stop_name_d = {}    # dictionary of stop_ids with stop_name as value
transfer_d = {}     # dictionary of stop_id with value as list of bus_ids that use this stop
start_stops = []    # list of stops that start a route
transfer_stops = []  # List of stops used for bus line transfers
end_stops = []      # list of stops the end a route
bad_optional_stops = []  # list of stops wrongly flagged as optional

bus_d = json.loads(input())     # read JSON data into dictionary
for d in bus_d:                 # step thru each bus_id record...
    stop_name_d[d['stop_id']] = d['stop_name']  # Build stop_name lookup table
    transfer_d.setdefault(d['stop_id'], []).append(d['bus_id'])  # Build list of bus_ids visiting a stop
    if d['stop_type'] == 'S':
        start_stops.append(d['stop_id'])    # build list of start stop_ids
    if d['stop_type'] == 'F':
        end_stops.append(d['stop_id'])      # build list of finish stop_ids
for sid, l_list in transfer_d.items():  # loop through the stop_id lists
    if len(l_list) > 1:
        transfer_stops.append(sid)      # and build list of transfer stops
# Now go back and run thru the busline JSON data again and check optional stop_ids not listed
optionals_ok = True
for d in bus_d:
    if d['stop_type'] == 'O':           # is this an Optional stop?
        if d['stop_id'] in chain(start_stops, end_stops, transfer_stops):
            bad_optional_stops.append(stop_name_d[d['stop_id']])
            optionals_ok = False        # error if also in the start, stop or transfer lists
print('On demand stop test:')
if optionals_ok:
    print('OK')
else:
    print(f'Wrong stop type: {sorted(bad_optional_stops)}')
