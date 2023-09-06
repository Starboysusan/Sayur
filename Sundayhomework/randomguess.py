#Import random module or package
import random
#Randomly numeber will be generated
computerNo=random.randint(100,110)

#inititalize variable to count the attempt
attemt=0

#Loop to continue the both have the correct number guesses
while(True):
    #Asking the input guess from user
    userNo=int(input("Enter the numbers:"))
    #If guess is low
    if(userNo<computerNo):
        print("Your guess is low")
    #if guess is correct
    elif(userNo==computerNo):
        print("Your guess is correct")
        break
    #if guess is high
    else:
        print("Your guess is high")
    attemt+=1   

#Final output display
print(f"User guess the number in {attemt} chance and the random number is {computerNo}")
