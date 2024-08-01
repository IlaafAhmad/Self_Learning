# Numbers divisible by 5 and 7

print("The numbers divisble between by 5 and 7 are ", end="")

for num in range(1499, 2500):
    if num % 5 == 0 and num % 7 == 0:
        print(num, end=" ")