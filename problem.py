"""

### Problem

Calendar Double Booking Conflicts

At Voyajoy, each home that we manage is listed on multiple short-term rental platforms like Airbnb and VRBO/Homeaway. We put it on multiple rental platforms because it helps listings reach more potential renters. Listing on multiple platforms, however, is a problem because each platform maintains its own calendar that are not synced with each other which leads to potential double bookings. Because of that, we need a way to detect double bookings for each listing. Please develop an algorithm that takes calendar events from multiple calendars and return a list of conflicting events.

Input: Two lists of events in json format

[
    { "name": "Booking Event Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"},
    ...
]

[
    { "name": "Booking Event A", "checkIn": "2016-07-07", "checkOut": "2016-07-14"}
    ...
]


Output: List of conflicting events

[
    [
        { "name": "Booking Event Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"},
        { "name": "Booking Event Bar", "checkIn": "2016-07-07", "checkOut": "2016-07-14"}
    ],
    ...
]

First figure out the different types of conflicts that can happen and then run some test data once you have your algorithm written. 

NOTE: checkIn of one event can match the checkOut of another event. This is because generally, a guest can checkout on the same day another guest checks in
"""

airbnb_cal = [
    { 'name': 'Booking Event Foo', 'checkIn': '2016-07-12', 'checkOut': '2016-07-19'},
    { 'name': 'Booking Event Bar', 'checkIn': '2016-07-22', 'checkOut': '2016-07-24'},
    { 'name': 'Booking Event Baz', 'checkIn': '2016-07-26', 'checkOut': '2016-08-05'},
    { 'name': 'Booking Event Paz', 'checkIn': '2016-08-05', 'checkOut': '2016-08-09'}
]

vrbo_cal = [
    { 'name': 'Booking Event A', 'checkIn': '2016-07-07', 'checkOut': '2016-07-14'},
    { 'name': 'Booking Event B', 'checkIn': '2016-07-16', 'checkOut': '2016-07-22'},
    { 'name': 'Booking Event C', 'checkIn': '2016-07-24', 'checkOut': '2016-07-26'},
    { 'name': 'Booking Event D', 'checkIn': '2016-08-06', 'checkOut': '2016-08-07'},
]

"""
expected_conflicts = [
    [
        { 'name': 'Booking Event Foo', 'checkIn': '2016-07-12', 'checkOut': '2016-07-19'},
        { 'name': 'Booking Event A', 'checkIn': '2016-07-07', 'checkOut': '2016-07-14'}
    ],
    [
        { 'name': 'Booking Event Foo', 'checkIn': '2016-07-12', 'checkOut': '2016-07-19'},
        { 'name': 'Booking Event B', 'checkIn': '2016-07-16', 'checkOut': '2016-07-22'},
    ],
    [
        { 'name': 'Booking Event Paz', 'checkIn': '2016-08-05', 'checkOut': '2016-08-09'},
        { 'name': 'Booking Event D', 'checkIn': '2016-08-06', 'checkOut': '2016-08-07'}
    ]
]
"""

# Please complete this function
def detect_conflicts(c1, c2):
    return list()

