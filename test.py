from unittest.mock import patch
from unittest import TestCase
import os

test_dir = 'test/'

test_data = {
	'test1.txt': 'PLACEHOLDER',
	'test2.txt': 'PLACEHOLDER2',
	'test3.txt': """PLACEHOLDER
	PLACEHOLDER
		PLACEHOLDER""",
	'test4.txt': 'PLACEHOLDER\nPLACEHOLDER'
}

def test_setup():
	"""Sets up test files in test directory."""
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	for k, v in test_data.items():
		with open(test_dir + k, 'w') as f:
			f.write(v)

def remove_tests():
	"""Removes test files and directory."""
	for k, v in test_data.items():
		os.remove(test_dir + k)
	try:
		os.rmdir(test_dir)
	except OSError:
		pass

def main():
	test_setup()
	remove_tests()

main()