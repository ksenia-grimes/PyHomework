a = 'beautiful'
b = 'racecar'
def Palindrome(word):
	if word == word[::-1]:
		return ('Yay! It\'s a Palindrome!')
	else:
		return ('Nope, it\'s not :(')
print(Palindrome(a))
print(Palindrome(b))
