def get_word(sentence, n):
	sentence=sentence.split()
	if len(sentence)>n and n>0:
		return sentence[n-1]
	else:
		sentence="Nothing"
		return sentence

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing