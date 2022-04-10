class Solution:
	def validPalindrome(self, s: str) -> bool:
		a = s[::-1]
		n=""
		m=""
		o=""
		p=""
		for x in range(len(s)):
			if s[x] != a[x]:
				n = a[:x] +  a[x+1:]
				b = len(s)-(x+1)
				m = s[:b] + s[b+1:]
				o = s[:x] + s[x+1:]
				b = len(s)-(x+1)
				p= a[:b] + a[b+1:]
				break
		return n==m or o==p