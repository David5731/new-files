import Mymodule
b = Mymodule.person1["country"]
print(b)
#the above code uses the def function from the mymodule.py

import Mymodule as CX9
a = CX9.person1["age"]
print(a)
#the above code renames Mymodule to CX9 then calls it

import platform
x = platform.system()
print(x)
#the above code utilises the platform module to check the name of your system 

from Mymodule import person1
print(person1["name"])
#the above code brings out only the name as output

import datetime
x = datetime.datetime.now()
print(x)
#the above code outputs the date, time, millisecond and second.

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#the above code brings out only the date and day from teh date

import datetime
x = datetime.datetime(2022, 6, 17)
print(x)
#the above code creates a custom datetime

