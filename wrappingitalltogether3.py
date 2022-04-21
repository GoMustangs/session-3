import random

equationList=[]
rightAnswerList=[]
userAnswerList=[]
correct=0

for x in range(0,10):

    op = random.randrange(0,3) # random values for oporators

    randomNumber1 = random.randrange(1,10) # generating random numbers
    randNum1 = int(randomNumber1)

    randomNumber2 = random.randrange(11,20)
    randNum2 = int(randomNumber2)

    if op == 0:

        rightAnswer= randNum1 + randNum2

        rightAnswerList.append(rightAnswer)

        print(randNum1, "+", randNum2)

        equationList.append(randNum1)
        equationList.append("+")
        equationList.append(randNum2)
        equationList.append("next equation")

        yourAnswer = int(input("what's your answer?: "))

        userAnswerList.append(yourAnswer)

        if yourAnswer == rightAnswer:
            correct+=1
    if op == 1:

        rightAnswer= randNum1 - randNum2

        rightAnswerList.append(rightAnswer)

        print(randNum1, "-", randNum2)

        equationList.append(randNum1)
        equationList.append("-")
        equationList.append(randNum2)
        equationList.append("next equation")

        yourAnswer = int(input("what's your answer?: "))

        userAnswerList.append(yourAnswer)

        if yourAnswer == rightAnswer:
            correct+=1
    
    if op == 2:

        rightAnswer= randNum1 * randNum2

        rightAnswerList.append(rightAnswer)

        print(randNum1, "x", randNum2)

        equationList.append(randNum1)
        equationList.append("x")
        equationList.append(randNum2)
        equationList.append("next equation")

        yourAnswer = int(input("what's your answer?: "))

        userAnswerList.append(yourAnswer)

        if yourAnswer == rightAnswer:
            correct+=1

print("here are the quations: ", equationList)
print("here are your answers: ", userAnswerList)
print("here are the right answers: ", rightAnswerList)
print("here's how many you got right: ", correct)