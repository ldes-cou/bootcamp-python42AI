def text_analyzer(*args):
	import string
	p = 0
	l = 0
	u = 0
	s = 0
	if len(args) > 1:
		print("ERROR")
		exit()
	elif len(args) < 1:
		str = input("What is the text to analyse?\n>>")
	else:
		str = args[0]
	for i in str:
		if i in string.punctuation:
			p += 1
		if i in string.ascii_lowercase:
			l += 1
		if i in string.ascii_uppercase:
			u += 1
		if i == ' ':
			s += 1
		i = len(str)
	print("The text contains ", i ,"characters:")
	print("-", p, "punctuations mark")
	print("-", l, "lowercase characters")
	print("-", u, "uppercase characters")
	print("-", s, "spaces")

text_analyzer()