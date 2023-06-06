#Basico 
for num in range(151):
    print(num)

#Multiplos de 5
for num in range(5, 1001, 5):
    print(num)

#Contar a manera del Dojo
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

#impares 
sum_imp = 0
for num in range(1, 500001, 2):
    sum_imp += num
print(sum_imp)


#cuenta regresiva de a 4 
for num in range(2018, 0, -4):
    print(num)
    

#contador flexible
numBaj = 2
numAlt = 9
mult = 3

for num in range(numBaj, numAlt + 1):
    if num % mult == 0:
        print(num)