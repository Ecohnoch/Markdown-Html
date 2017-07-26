import re
lines = ['[image](http://i4.piimg.com/1949/66a86de9c5c16aa8.png)f**sf**![asf](http://i4.piimg.com/1949/66a86de9c5c16aa8.png)'
]

# <img src="http://i4.piimg.com/1949/66a86de9c5c16aa8.png" alt="image">
def parseImage(test):
	while(re.search(r'\!\[(.*?)\]\((.*?)\)', test) != None):
		obj = re.search(r'\!\[(.*?)\]\((.*?)\)', test)
		print(obj)
		text1 = ""
		text2 = ""
		if obj.span(0)[0] == 0:
			pass
		else:
			text1 = test[: obj.span(0)[0]]

		if obj.span(0)[1] == len(test) - 1:
			pass
		else:
			text2 = test[obj.span(0)[1] + 1:]
		test = text1 + "<p><img src=\"" + obj.group(2) + "\" alt=\"" + obj.group(1) + "\"></img></p>" + text2
	return test

print(parseImage(lines[0]))