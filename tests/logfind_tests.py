from nose.tools import *
import logfind

def setUp():
    #super(logfind_tests, self).setUp()
    print "SETUP!"

def teardown():
    #super(logfind_tests, self).tearDown()
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"