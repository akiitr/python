# This is a module which will use the fuction defined in the pre defined modules
# Anubhav

import 	mod
from mypackage.mod1 import *
from mypackage.mod2 import *
print ("Now in the main of app.py with the value of __name__ as: " + __name__)
mod.f1()
mod.f3()
print ("Imported from the mypackage module1 or mod1.py")
f1() 
print ("Imported from the mypackage module2 or mod2.py") 
f2()
