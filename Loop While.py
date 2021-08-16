# counter = 1
# while counter <= 10 :
#     print(counter)
#     counter += 1

# counter = 1
# while counter <= 20 :
#     if (counter % 2) == 0 :
#         print(counter)
#     counter += 1

num = int(input("Enter number : "))
numRev = 0
while num != 0 :
    temp = int(num % 10)
    num = int(num / 10)
    numRev = (numRev * 10) + temp

print("--------------------------")
print("Rev : " , numRev)