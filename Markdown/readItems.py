import os
import shutil
def readQuoteStyle():
	f = open("quoteStyle.css", 'r')
	ans = ""
	try:
		ans = f.read()
	finally:
		f.close()
	return ans + "\n"

def readCodeStyle():
	f = open("codeStyle.css", 'r')
	ans = ""
	try:
		ans = f.read()
	finally:
		f.close()
	return ans + "\n"

def readCodeJS():
	f = open("codeJS.css", 'r')
	ans = ""
	try:
		ans = f.read()
	finally:
		f.close()
	return ans + "\n"

def readSourceMD(filename):
	f = open(filename, 'r')
	ans = ""
	try:
		ans = f.read()
	finally:
		f.close()
	return ans + "\n"

def output(html, filename):
	if os.path.exists('output'):
		pass
	else:
		os.mkdir('output')
	shutil.copy('prism.css', './output')
	shutil.copy('prism.js', './output')

	f = open('./output/' + filename, 'w')
	f.write(html)
	f.close()