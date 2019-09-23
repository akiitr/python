def collatz(num):
	if (num % 2 == 0):
		print (num // 2)
		return collatz(num // 2)
	elif (num == 1):
		print (num)
		return
	else:
		print (3* num + 1)
		return collatz (3*num + 1)

print('Enter a no of reducing it to 1')
try:
	nu = int(input())
except:
	print ('Please enter intgar only')

collatz(nu)
print("see I told you it will come back to 1 with any no input Thank you!!")
