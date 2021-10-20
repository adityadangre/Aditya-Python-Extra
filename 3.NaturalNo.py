rangeofnumber = int(input('Enter the range of the number: '))
count = 0

for i in range(rangeofnumber):
    if(count % 2) == 0:        
        print(count)
    elif(count % 4) == 0: 
        print(count)

    count = count + 1