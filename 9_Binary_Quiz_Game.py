score = 0 
total_Question1 = 0
total_Question = 0
import pyttsx3
engine = pyttsx3.init()
engine.say('''Welcome to the Quick Binary revsion, 
        it wil recall binary number line.\t
        ------ All The Best ------\t\t
        Instruction\t\t\t
        1. If you type 3 it will break your Quiz.\b
        2. There are two rounds.\b
        3. Give right answer to to every Question else you will be subtrated.''')
engine.runAndWait()
import random # It is a moudle which takes random.
print('''Welcome to the Quick Binary revsion, 
        it wil recall binary number line.\t
        ------ All The Best ------\t\t
        Instruction\t\t\t
        1. If you type 3 it will break your Quiz.\b
        2. There are two rounds.\b''')# It will the Welcome to Binary Quiz.
b = int(input('How many quetsion do you want solve: '))
while True: #It is loop with code.
                r = random.randint(0,100) #It will take a random number.
                n = int(bin(r)[2:]) # It will convert the random number into binary number. 
                c = print(f'convert {r} into binary.') #It will print the random number.
                a = int(input('Enter the binary number: ')) #It will take the binary number from user.
                if(a==3):# If we will type 'exit' then it will print your score,total question,wrong answer and right answer
                    break
                elif(a==n): # It will check wether you are right or wrong or keyboard error occurred.
                    print('✅You are right.KEEP IT UP....')
                    score+=1
                    total_Question+=1
                elif(a!=n):
                    print(f'❌ You are incorrect. The actual answer is {n} ')
                    total_Question+=1
                else:
                    print('Keyboard Error occured..... ')
                    break
                if (total_Question==b):
                    choice = input('your attempt get over.do you want continue [y/n]').lower()
                    if(choice!='y'):
                            break
                    elif(choice=='y'):
                            b1 = int(input('How many quetsion do you want solve: '))
                            r = random.randint(0,100) #It will take a random number.
                            n = int(bin(r)[2:]) # It will convert the random number into binary number. 
                            c = print(f'convert {r} into binary.') #It will print the random number.
                            a = int(input('Enter the binary number: ')) #It will take the binary number from user.
                            if(a==3):# If we will type 'exit' then it will print your score,total question,wrong answer and right answer
 
                                break
                            elif(a==n): # It will check wether you are right or wrong or keyboard error occurred.
                                print('✅You are right.KEEP IT UP....')
                                score+=1
                                total_Question1+=1
                            elif(a!=n):
                                print(f' ❌ You are incorrect. The actual answer is {n} ')
                                total_Question1+=1
                            else:
                                        print('Keyboard Error occured..... ')
                                        break
                            if(total_Question1==b1):
                                        break
print(f'''final report
score = {int(score)}\b
total question {int(total_Question+total_Question1)}\b
wrong answer {int(total_Question+total_Question1 - score)}\b
right answer {int(score)}\b
thank you binary ninja.''')
print('Program overed...'
      'Run it again.....\t') 