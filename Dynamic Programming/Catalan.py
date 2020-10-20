#QUESTION:
#Program for nth Catalan Number
#Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems.

#Catalan numbers satisfy the following recursive formula. 
 C_0=1 \ and \ C_n_+_1=\sum_{i=0}^{n}C_iC_n_-_i \ for \ n\geq 0;    

#CODE:
#RECURSIVE SOLN:
def catalan(n):
	if n <= 1:
		return 1

	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n - i - 1)

	return res
  
#DP SOLN:
def catalan(n):
	if n == 0 or n == 1:
		return 1

	pre = [0]*(n + 1)
	pre[0], pre[1] = 1, 1

	for i in range(2, n + 1):
		pre[i] = 0
		for j in range(i):
			pre[i] = pre[i] + pre[j] * pre[i - j - 1]
	
	return pre[n]

n = int(input())
print(catalan(n))
  
