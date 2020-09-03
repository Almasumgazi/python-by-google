def letter__spacing(no_of_spaces,string):
	result=no_of_spaces.join(string)
	return result

def number__spacer(no_of_space,space):
	result=no_of_space*space
	return result

space=" "
no_of_space=0

string="hi there"
no_of_spaces=number__spacer(no_of_space,space)


print(letter__spacing(no_of_spaces,string))