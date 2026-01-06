#Calculate Average Temperature
"""numdays=int(input("How many days's Temperature?.."))
total=0
temp=[]
for i in range(numdays):
  nextday=int(input("Day"+str(i+1)+"'s high temp"))
  temp.append(nextday)
  total+=temp[i]
avg=round(total/numdays,2)
print("\nAverage="+str(avg))"""

numdays = int(input("How many days' Temperature? "))
total = 0
temp = []

for i in range(numdays):
    nextday = int(input(f"Day {i+1}'s high temp: "))
    temp.append(nextday)
    total += nextday

avg = round(total / numdays, 2)
print("\nAverage =", avg)



