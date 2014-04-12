import re

def count(string):
	counter = {}

	string = re.sub(r'[^a-zA-Z-]+', ' ', string)

	words = string.lower().split(' ')
	for word in words:
		if not word:
			continue

		if word not in counter:
			counter[word] = 0
		counter[word] += 1
	return counter


def count_file(filename):
	with open(filename) as f:
		return count(f.read())



