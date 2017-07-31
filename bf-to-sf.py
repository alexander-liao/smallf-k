bf = input()
codes = '+-,.<>[]'
index = 0
string = ''
for code in bf:
	if code in codes:
		while codes[index] != code:
			index = (index + 1) % 8
			string += '+'
		string += '@'
print(string)
