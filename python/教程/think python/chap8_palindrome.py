#测试字符串是否是回文的。
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i = 0 
	j = len(word2)

	while j > 0:
		if word1[i] != word2[j]:
			return False
		i = i + 1
		j = j + 1

	return True

#判断字符串是否回文时这个函数的特例
def is_palindrome_2(word):
	return is_reverse(word, word)

print(is_palindrome("allen"))
print(is_palindrome("bob"))

print(is_palindrome("otto"))

print(is_palindrome("redivider"))


