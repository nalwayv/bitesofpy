"""
Bite 67. Working with datetimes
This Bite involves solving two problems using datetime:

We kicked off our 100 Days of Code project on March 30th, 2017. 
Calculate what date we finished the full 100 days!
PyBites was founded on the 19th of December 2016. 
We're attending our first PyCon together on May 8th, 2018. 
Can you calculate how many days from PyBites' inception to our first PyCon meet up?

"""

from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    date = start_100days + timedelta(days=100)
    return str(date)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    days_total = (pycon_date - pybites_founded).days
    return days_total
