import random
i = 10
comp_pnt = 0
user_pnt = 0

list1 = ['Snake','Water','Gun']
while i > 0:
    choice = random.choice(list1)
    i-=1
    userch = input('Enter Snake or Water or Gun')
    if choice == 'Snake' and userch == 'Water':
        comp_pnt+=1
    elif choice == 'Snake' and userch == 'Gun':
        user_pnt+=1
    elif choice == 'Water' and userch == 'Snake':
        user_pnt+=1
    elif choice == 'Water' and userch == 'Gun':
        comp_pnt+=1
    elif choice == 'Gun' and userch == 'Snake':
        comp_pnt+=1
    elif choice == 'Gun' and userch == 'Water':
        user_pnt+=1
    else:
        continue
if comp_pnt > user_pnt:
    print(f'Computer won the game')
elif user_pnt > comp_pnt:
    print(f'You won     the game')
else:
    print('Its a tie')
print(f'Computer won {comp_pnt} times')
print(f'You won {user_pnt} times')








