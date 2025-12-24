def first_second(my_list):
  max1,max2=float('-inf'),float('-inf')
  for num in my_list:
    if num>max1:
      max2=max1
      max1=num
    elif num>max2 and num!=max1:
      max2=num
  return max1,max2
my_list=[81,82,83,78,98,100]
print(first_second(my_list))