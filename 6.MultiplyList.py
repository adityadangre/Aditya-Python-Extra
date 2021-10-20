def MUL(NumList):
    mul = 1
    print("Multiplication of ", end = " ")

    for num in NumList:
        print(num, end = " * ")
        mul = mul * num
    
    print(" = ", mul)

print("Welcome")
NumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MUL(NumList)