def email__formatter(l1,l2):
	new_list=[]
	lis=[]
	lis.append(l1)
	lis.append(l2)
	for name,email in lis:
		new_list.append("{} <{}>".format(name,email))
	return new_list
	
	# for i in range(0,len(l1)):


l1=('naman','taman','jaman')   #naman<naman@gmail.com> 
l2=('naman@gmail.com','taman@gmail.com','jaman@gmail.com')

print(email__formatter(l1,l2))