# predict_ical
A quick Python script to generate an ical for weather satellite passes, that can then be imported into the calendar app of your choosing. Quick, dirty, and hacky, this is some of my worst Python work. But it does work.

## Dependencies

An installation of `predict` is required, as well as the `icalendar` Python module.

## Setup

Create the file `station.qth` that contains a name for the base station, then the longitude, latitude, and elevation each on their own lines. This is in the Predictor format, so lat is positive for N and negative for S, and long is positive for W and negative for E. An example file for downtown LA is below: 
```
DTLA
 34.054823
 118.24613
 95
```

Then, in `main.py`, set the `SATS`, `FREQS`, and `THRESHOLD` variables to their desired values. `SATS` is an array of satellites that you want to track, `FREQS` is a dictionary that contains the frequencies for each satellite, and `THRESHOLD` is the minimum elevation in degrees required to create an event for the pass.

## Usage
`python main.py` will lead to the creation of a `calendar.ics` file that works in Google Calendar and the like
