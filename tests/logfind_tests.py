from hamcrest import *

from logfind.logfind import LogFind


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_home_folder():
    home = LogFind().get_home()
    assert_that(home, equal_to("C:\Users\Milan"))