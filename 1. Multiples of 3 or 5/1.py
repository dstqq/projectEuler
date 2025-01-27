# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

i = 1
result = 0
while (i*3 < 1000):
    result += i*3
    i+=1


i = 1

while (i*5<1000):
    if i % 3 != 0:
        result += i*5
    i+=1

print(result)

res = 0
count = 3
while count < 1000:
    if count % 3 == 0 or count % 5 == 0:
        res += count
    count += 1
    
print(res)