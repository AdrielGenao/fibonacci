numbers=[0,1]
x=0
while x<10:  # Change this number to show different amount of numbers
    next=numbers[x]+numbers[x+1]
    numbers.append(next)
    print(numbers[x])
    x+=1

