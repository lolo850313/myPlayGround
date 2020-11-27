#判断一个int树从start开始后len的长度，是否为回文。
def has_palindrome(i, start, len):
	s = str(i)[start : start + len]
	return s == s[::-1]

def check(i):
	return (has_palindrome(i,2,4) and has_palindrome(i+1,1,5) and has_palindrome(i+2,1,4) and has_palindrome(i+3,0,6))

def check_all():
	#999996 + 3 后是最大的6位数
	for i in range(100000,999996):
		if check(i):
			print(i)

check_all()