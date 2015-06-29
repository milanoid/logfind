import argparse
import os


class logfind(object):

	def __init__(self):
		pass

	def get_home(self):
		return os.path.expanduser('~')

def main():
	print logfind().get_home()

if __name__ == "__main__":
	main()
