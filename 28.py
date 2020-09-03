def combine_lists(list1, list2):
  new_list=[]
  list1.reverse()
  new_list=list2+list1
  return new_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
