# duplicate numbers
def remove_duplicates(lst):
  unique_lst=[]
  seen=set()
  for item in lst:
    if item not in seen:
      unique_lst.append(item)
      seen.add(item)
  return unique_lst
my_list=[1,1,2,3,4,4,5,6,7,8,9]
print(remove_duplicates(my_list))