from get_passes import get_passes
from generate_file import generate_file
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime

cal = Calendar()
cal.add('prodid', '-//My calendar product//example.com//')
cal.add('version', '2.0')

SATS = ["NOAA-15", "NOAA-18", "NOAA-19"]
FREQS = {
        "NOAA-15": "137.6200",
        "NOAA-18": "137.9125",
        "NOAA-19": "137.1000"
        }
THRESHOLD=70

def add_sat_to_ical(cal, sat):
    generate_file(sat)
    passes = get_passes(THRESHOLD)

    for sat_pass in passes:
        event = Event()
        event.add('name', sat)
        event.add('summary', sat)
        event.add('description', f"Frequency {FREQS[sat]}. Max Elevation {sat_pass['max_elev']}")
        event.add('dtstart', datetime.fromtimestamp(int(sat_pass['start_time'])))
        event.add('dtend', datetime.fromtimestamp(int(sat_pass['end_time'])))
        event['uid'] = sat_pass['start_time'] + sat + "@example.com"
        event['location'] = vText('San Diego, CA')
        event['organizer'] = vCalAddress('MAILTO:p@example.com')
        cal.add_component(event)

for sat in SATS:
    add_sat_to_ical(cal, sat)

with open("calendar.ics", "wb+") as f:
    f.write(cal.to_ical())
