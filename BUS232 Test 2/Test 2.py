f = open('C:/Users/wib/Desktop/vision project 2/texture results/New folder/shareholders.txt', 'w')
def listsum(arr):
  sum = 0
  for i in range(len(arr)):
    sum = sum + arr[i] 
  return sum


a=1
holders = []

while a != 0:
  a = int(input("Please enter the number of shares: "))
  holders.append(a)
  f.write("Please enter the number of shares: " + str(a) + "\n")

sum = listsum(holders)

f.write("Thank you, there is a total of " + str(sum) + " shares represented here.\n")
print("Thank you, there is a total of" , sum , "shares represented here.")
f.write("Shared needed for majority vote is " + str(int((sum)/2)+1) + "\n")
print("Shared needed for majority vote is" , int((sum)/2)+1)

holders.sort()
a = 0
counter = 0

while (int((sum)/2)+1) > a:
  a = a + holders[-counter]
  counter = counter + 1


print("You need the support of top ", counter-1, " shareholders for this number of votes")
f.write("You need the support of top " + str(counter-1) + " shareholders for this number of votes")
f.close()