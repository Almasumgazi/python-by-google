def is_palindrome(input_string):
	# We'll create two strings, to compare them
	x=input_string.strip().lower()
	x=x.replace(" ","")
	rev=x[::-1]
	if rev==x:
		return True
	else:
		return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True