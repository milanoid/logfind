from nose.tools import *
from hamcrest import *
from logfind.logfind import logfind

def setUp():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_home_folder():
    home = logfind().get_home()
    assert_that(home, equal_to("C:\Users\Milan"))