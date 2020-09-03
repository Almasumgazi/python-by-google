filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames=[]
for file in filenames:
	name,extension=file.split(".")
	if extension=="hpp":
		x=name+"."+"h"
		newfilenames.append(x)
	else:
		x=name+"."+extension
		newfilenames.append(x)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]