#!/usr/bin/env python
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	print original
else:
	print 'empty'
word = original.lower()
first = word[0]
new_word = word + pyg
if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U':
	print new_word
new_word = word[1:] + word[0] + pyg
if first != 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U':
	print new_word