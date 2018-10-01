#! python3
import pyperclip
import time
import sys

text = ''
flag = True
content = []

def getText():
	try:
		text = str(pyperclip.paste())
	except:
		text = ''
	return text

def setFlag(prevText):
	if prevText == getText():
		flag = False
	else:
		flag = True
	return flag

def showHelp():
	print("This is going to be the help")

def combine():
	global content
	text = ''
	for element in content:
		text = text + '\n' + str(element)
	print(text)
	pyperclip.copy(text)
	print('[+] Combined text copied to clipboard\n')

def selectiveCombine():
	selection = input('>>>>>> ')
	selectionData = list(map(int, selection.split()))
	global content
	text = ''
	j = 1
	for element in content:
		if j in selectionData:
			text = text + '\n' + str(element)
		j = j + 1
	print(text)
	pyperclip.copy(text)
	print('[+] Seletively combined text copied to clipboard\n')

def showContent():
	global content
	j = 1
	for i in content:
		print('[{}] '.format(j)+i)
		j=j+1

def getClipboardContent(quick=False):
	global text, flag, content
	try:
		while 1:
			flag = setFlag(text)
			if flag:
				text = getText()
				if text == '':
					pass
					# print("No text in clipboard")
				else:
					content.append(text)
					flag = False
			# The following sleep is only meant to make the break procedure
			# using 'ctrl + c' effective
			time.sleep(1)
	except KeyboardInterrupt:
		print (content)
		print ('[+] Done Copying\n')
		if quick:
			combine()

if __name__ == '__main__':
	while True:
		choice = input('[][][] ')
		if choice.lower() == 'help':
			showHelp()
		if choice.lower() == 'start':
			getClipboardContent()
		if choice.lower() == 'quick':
			getClipboardContent(True)
		if choice.lower() == 'show':
			showContent()
		if choice.lower() == 'combine':
			combine()
		if choice.lower() == 'selective':
			selectiveCombine()
		if choice.lower() == 'exit':
			sys.exit()
		time.sleep(1)

		



