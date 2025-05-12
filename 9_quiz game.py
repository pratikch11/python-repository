score = 0
total_Question = 0
l = { 
    "42":101010,
    "24":11000,
    "32":100000,
    "45":101101,
    "23":10111,
    "67":100011,
    "56":1010110,
    "34":100010,
    "78":1001110,
    "92":1011100}
print('''Welcome to the Quick Binary revsion.
        It wil recall binary number line.\n\n\n\t
      ------ All The Best ------\n\n\n\t''')
print('These are the keys of binary number:-')
for item in l:
    print(item)
while True:
    a = input('Enter a key given above:- ')
    a2 = int(input('Enter the binary number:---\nans=\t'))

    if (a2==l[a]):
            print('Correct! you are given right answer.')
            score+=1
            total_Question+=1
    else:
        print(f'Incorrect! your answer is {l[a]}')
        total_Question+=1
    
    if(total_Question==4):
        choice=input("do you wish to continue?[Y/N]")
        if choice. lower()=="n":
            print('program finished')
            print(f'''Thank you
                        score = {int(score)}
                        total question {int(total_Question)}
                        wrong question {total_Question - score}
                        right answer {score}''')
            break
        else:
            continue  
      