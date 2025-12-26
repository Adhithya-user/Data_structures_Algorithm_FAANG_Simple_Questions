#Find Number of Days Above Average Temperature
#Average
#above Average

#calculate Average
num_days=int(input("how many days"))
total=0
for i in range(1,num_days+1):
  nextDay=int(input(input("Day"+str(i)+"s high temp:")))
  total+=nextDay
avg=round(total/num_days,2)
print("\nAverage="+str(avg))
