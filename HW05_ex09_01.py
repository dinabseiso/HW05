#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def gargantuan():
	""" Takes in specific text file "words.txt," and scans it 
	line by line in search of words greater than 20 characters. 
	Contains a catch that I have commented out for prettiness'
	sake, as there are only three words that contain more than 
	20 characters in the list (others fall close, with character 
		lengths of 19 or so, otherwise exceeding 20 characters when 
		whitespace is included).
	"""

	fin = open("words.txt")
	line = fin.readline()
	for line in fin : 
		if len(line) > 20 : 
			try : 
				word = line.strip()
				if len(word) > 20 : 
					print word
#				else : 
#					print ("Almost got me there! Exclude whitespace.")
			except : 
				pass
		else : 
			continue

##############################################################################
def main():

    gargantuan()

if __name__ == '__main__':
    main()
