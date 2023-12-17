import random
import time
OPERATORS = ["+","-","*","//","%"]
MIN_OPERATOR = 3
MAX_OPERATOR  = 12
TOTAL_CHALLENGES = 10

def generate_challenge():
    left = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    operator = random.choice(OPERATORS)
    expersion = str(left)+" "+operator+" "+str(right)
    answer = eval(expersion)
    return expersion,answer

wrong = 0
input("Please enter to start")
print("---------------------")

start_time = time.time()

for i in range(1,TOTAL_CHALLENGES+1):
    expersion,answer = generate_challenge()
    while True:
        guess = input("Problem #" +str(i)+ " :  " +expersion + " = ")

        if guess == str(answer):
            break
        wrong += 1 
end_time = time.time()
total_time = round(end_time - start_time,2)
print("----------------------------")
print("Nice Work! You finshed in " + str(total_time)+ " seconds !")





