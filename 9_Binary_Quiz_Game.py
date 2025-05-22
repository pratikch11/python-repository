import random # It is a moudle which takes random.
score = 0 
total_Question = 0 
total_Question1 = 0
print('''Welcome to the Quick Binary revsion. 
        It wil recall binary number line.\n\n\n\t
        ------ All The Best ------\n\n\n\t''')# It will the Welcome to Binary Quiz.
b = int(input('How many quetsion do you want solve: '))
while True: #It is loop with code .
            r = random.randint(0,100) #It will take a random number.
            n = int(bin(r)[2:]) # It will convert the random number into binary number. 
            c = print(f'convert {r} into binary.') #It will print the random number.
            a = int(input('Enter the binary number: '))   #It will take the binary nu1mber from user.
            if(a == 'exit'): # If we will type 'exit' then it will print your score,total question,wrong answer and right answer
                print(f'''Thank you,
                        score = {int(score)}\b
                        total question {int(total_Question + total_Question1)}\b
                        wrong answer {int(total_Question + total_Question1 - score)}\b
                        right answer {int(score)}\b''')
                break
            if(a == n): # It will check wether you are right or wrong or keyboard error occurred.
                print('You are right.KEEP IT UP....')
                total_Question+=1
                score+=1
            elif(a!=n):
                print(f'You are incorrect. The actual answer is {n} ')
                total_Question+=1
            else:
                print('Keyboard Error occured..... ')
                break
            for i in range(total_Question==b): #It will ask when attempt get over which will ask do you want to coutinue or not.
                choice = input('your attempt get over.do you want continue [y/n]')
                if(choice=='n'):
                    print(f'''Thank you,
                        score = {int(score)}\b
                        total question {int(total_Question + total_Question1)}\b
                        wrong answer {int(total_Question + total_Question1 - score)}\b
                        right answer {int(score)}\b''')
                    break
                elif(choice == 'y'):
                    d = int(input('how more attempt do you want to do: '))
                    if(total_Question1 == d):
                        print(f'''Thank you,
                            score = {int(score)}\b
                            total question {int(total_Question + total_Question1)}\b
                            wrong answer {int(total_Question + total_Question1 - score)}\b
                            right answer {int(score)}\b''')
                        break
                    if(a==n):
                        score+=1
                        total_Question1+=1
                    if(a!=n):
                        total_Question1+=1 
                else:
                    print('Keyboard Error occured..... ')
                    break
print('''Program is Finished...\n 
      Run It Again....''')  #Then program get finished.             