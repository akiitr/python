#python module environment and  __name__ for conditoinal execution.



def f1():
	print("In function : F1")
def f2():
	print("In function : F2")
def f3():
	print("In function : F3")


print("Now in main module of mod.py with __name__ as: " + __name__)
if (__name__ == '__main__'):
		f1()
		f2()
		f3()
