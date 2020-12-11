a = 'beautiful'
b = 'racecar'
def Palindrome(word):
	word = word.lower().strip()#приведение к нижнему регистру и удаление пробелов по краям
	if word == word[::-1]:
		return ('Yay! It\'s a Palindrome!')
	else:
		return ('Nope, it\'s not :(')
print(Palindrome(a))
print(Palindrome(b))
