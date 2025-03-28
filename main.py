import random
n = random.randint(1,100)
a = -1
guess = 0

while(a!=n):
    guess+=1
    a = int(input("Guess a number: "))

    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
    

print(f"You have guessed the number correctly in {guess} in attempt")