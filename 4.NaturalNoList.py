l = []
i = 1

while i <= 200: 

    if(i % 20 == 0):
        l.append(i)
    i = i + 1  

print("Multiples of 20 in between 1 to 200 are:")

for j in l :
    print(j, end = "  ")