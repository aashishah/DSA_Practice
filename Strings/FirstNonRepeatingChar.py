#Time complexity: O(n^2):

def firstnonrepeating(s):
	for i in range(len(s)):
		duplicate_seen = False
		for j in range(len(s)):
			if s[i] == s[j] and i != j:
				duplicate_seen = True
				break
		if not duplicate_seen:
			return s[i]
	return '_'

#print(firstnonrepeating(input("Enter string: ")))

#Time complexity: O(2n) or O(n)

def firstnonrepeating_simp(s):
	freq = {}
	for i in range(len(s)):
		if s[i] in freq:
			freq[s[i]] += 1
		else:
			freq[s[i]] = 1

	for i in range(len(s)):
		if freq[s[i]] == 1:
			return s[i]

	return '_'

print(firstnonrepeating_simp(input("Enter string: ")))
