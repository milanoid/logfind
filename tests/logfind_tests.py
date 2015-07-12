from hamcrest import *

from logfind.logfind import LogFind


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_home_folder():
    home = LogFind().get_home()
    assert_that(home, equal_to("C:\Users\Milan"))


def test_can_open_config_file():
    user_home = LogFind().load_config_file()
    assert_that(user_home, has_item('regex1'))
    assert_that(user_home, has_item('regex2'))
    assert_that(user_home, has_item('regex3'))