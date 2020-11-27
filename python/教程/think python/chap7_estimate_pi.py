import math
def factorial(para):
	#k的阶乘
	mul = 1
	if para == 0:
		return 1
	while para >0:
		mul = mul*para
		para = para - 1
	return mul

def estimate_pi():
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4 * k) * (1103 + 26390 * k)
		den = factorial(k) ** 4 * 396**(4*k)
		term = factor * num / den
		total += term

		if abs(term) < 1e-15:break
		k += 1

	return 1 / total

print(estimate_pi())