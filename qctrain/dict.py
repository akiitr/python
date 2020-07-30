#python at QC
#anubhav

phonebook = {"ak": 1, "dk": 2, "pk": 3}

for name,phone in phonebook.items():
	print("Name: " + name.upper())
	print("Phone: " + str(phone))
	print("=======================")

name = input('Please enter the name to be added')
phone = input('Please enter the phone no for the user')
phonebook[name] = int(phone)

dname = input('Please enter the name(key) to be deleted')
if dname in phonebook.keys():
	del phonebook[dname]
	print('entry(key): ' + dname + 'has been deleted')
else:
	print('the keyerror the name do not exist')


print('this is the updated dictonary')
for name,phone in phonebook.items():
	print("Name: " + name.upper())
	print("Phone: "+ str(phone))
	print("=======================")
