def tig_latin(text):
	lst=[]
	words=text.split()
	for word in words:
		new_word= word[1:]+word[0]+"ay"
		lst.append(new_word)
		final__words=' '.join(lst)
	return final__words
		
print(tig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(tig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"