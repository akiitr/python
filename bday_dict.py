bday = { 'anubhav': '26 july', 'jai': '10th august' }
while True:
	print('enter the name of person for b\'day date or q to exit')
	name = input()
	if name == 'q':
		break
	
	if name in bday:
		print (bday[name] + 'is b\'day for' + name)
	else:
		print ('I do not have information please add this entry')
		print ('Please tell his birthdate')
		day = input()
		bday[name] = day
		print ('database updated!!')


