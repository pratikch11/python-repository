import random
r = random.randint(0,100)
n = bin(r)[2:]
score = 0
total_Question = 0
print('''Welcome to the Quick Binary revsion.
        It wil recall binary number line.\n\n\n\t
        ------ All The Best ------\n\n\n\t''')
b = int(input('How many quetsion do you want solve: '))
while True:    
            c = print(f'convert {r} into binary.')
            a = input('Enter the binary number: ')
            
            if(a == n):
                print('You are right.KEEP IT UP....')
                total_Question+=1
                score+=1
            else:
                print(f'You are incorrect.the actual answer is {n} ')
                total_Question+=1
            if(total_Question==b):
                choice = input('your attmept get over.do you want continue [y/n]')
                if(choice=='n'):
                    print('program finished')
                    print(f'''Thank you
                        score = {int(score)}\\b
                        total question {int(total_Question)}\\b
                        wrong question {total_Question - score}\\b
                        right answer {score}\\b''')
                    break
            else:
                continue       


             