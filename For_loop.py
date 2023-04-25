#for loop
print("_______number 0 to 9______________________")
for i in range(10):
    print(i)
print("_______number 1 to 20 ______________________")

for i in range(1,21):
    print(i)

print("___________even number__________________")

for i in range(2,20,2):
    print(i)

print("___________odd number__________________")

for i in range(1,21,2):
    print(i)

print("_____________________________")


for i in range(5):
    for j in range(i):
        print("*",end="")
    print(" ")
    


print("_____________________________")




for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print(" ")
