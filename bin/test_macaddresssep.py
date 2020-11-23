"""Test macaddresssep file
"""
from macaddresssep import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-23"

def test():
	"""Tests the macaddresssep function in the macaddresssep class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert macaddresssep.macaddresssep() == "macaddresssep", "test failed"
	#assert macaddresssep.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
