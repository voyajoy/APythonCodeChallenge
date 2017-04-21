## Coding Challenge

In order to be considered for this position, you must complete the following steps. 

*Note: This task should take no longer than 1-2 hours at the most.*


### Prerequisites

- Please note that this will require some basic knowledge and/or the ability to learn of the following:
       - Python
       - [Django](http://expressjs.com/)
       - Git
       - [Docker](http://www.docker.com/)
       - Any type of DB of your choosing

- You will need to have the following installed to complete this task
       - Python
       - [Docker](http://www.docker.com/)
       - Azure

## Task

1. Fork this repository
2. Create a *source* folder to contain your code. 
3. In the *source* directory, please create an Django app that accomplishes the following:
    - Create a function(s) that solves the coding problem in the next section below
    - Create an API that allows you to post two lists of the events as specified in the Problem section below and returns the list of conflicting events. Use JSON.
    - Write tests that adequately test the functionality.
4. Dockerize your application by writing a docker.yml file and test it by running the container locally.
5. Commit and Push your code to your new repository
6. Send us a pull request, we will review your code and get back to you
7. Deploy this docker image to Azure. I will need to give you access to this via skype or email.

### Problem

**Also located in problem.py**

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

### Tests

Create the following unit tests with the testing framework of your choice:

  1.  Write a few tests that tests the above problem. Write as little or as many tests as you see that is appropriate.

## Once Complete
1. Commit and Push your code to your new repository
2. Send us a pull request, we will review your code and get back to you

### Notes
- You are free to write and modularize code any way you like just as long as you follow the requirements
- 4 spaces for indentation! No tabs!
- If you don't know how to do something, Google is your friend!
- If you have any questions or need clarifications, please do not hesitate to reach me at ivan@voyajoy.com or @ ivan.voyajoy on Skype.