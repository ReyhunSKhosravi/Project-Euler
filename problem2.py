def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

sum = 0
first = 1
second = 2
while(first < 4 * 10 ** 6):
    if(isEven(first)):
        sum += first
    new = first + second
    first = second
    second = new
print(sum)