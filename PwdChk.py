symbols = ['!','@','#','$','%','^','_','+','-','=','?','&','*']

#Option 1 - Password Strength Checker
def PSC(pwd):
    c_symbol, c_number, c_low_case, c_upp_case = 0, 0, 0, 0
    for i in pwd:
        if i in symbols:
            c_symbol += 1
        elif ord(i) in range(0,10):
            c_number += 1
        elif ord(i) in range(65,91):
            c_low_case += 1
        elif ord(i) in range(97,123):
            c_upp_case += 1
    if (len(pwd)>11) and c_symbol>0 and c_number>0 and c_low_case>0 and c_upp_case>0 :
        return 'STRONG'
    elif (len(pwd)>=8 and len(pwd)<=11) and ((c_symbol>0 and c_number>0 and c_low_case>0) or (c_symbol>0 and c_number>0 and c_upp_case>0) or (c_symbol>0 and c_low_case>0 and c_upp_case) or (c_number>0 and c_low_case>0 and c_upp_case>0)):
        return 'MODERATE'
    else :
        return 'POOR'


#Option 2
def RPG():  
    pwd = ""
    for i in range(0,3):
        pwd += str(random.randint(0,9))
        pwd += chr(random.randint(65,90))
        pwd += chr(random.randint(97, 122))
        pwd += str(random.choice(symbols))
    k=list(pwd)
    random.shuffle(k)
    return ''.join(k)


#Option 3 - End with credits to the author
def ETP():
    print('This program is courtesy of: Shravan \n')


def main():
    inp = int(input('''\nChoose from the following set of options to be executed: 
    1. Password Strength Checker
    2. Random Password Generator for a given Username
    3. End the program
Enter your choice: '''))

    if inp == 1:
        count = 0
        op = open('Users-Pwds.txt', 'r') 
        out = open('Users-Pwds-Chked.txt','w+')
        lines = op.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            username, pwd = line.split(',')
            count += 1
            strength = PSC(pwd)
            out.write(username+','+pwd+','+strength+'\n')
        print(f"The total number of passwords checked are: {count} and the password strengths are written into 'Users-Pwds-Chked.txt' file.")
        main()

    elif inp == 2:
        username = input('Enter the username to generate the password : ')
        while username is None or len(username)>20:
            print("The username can't be empty or greater than 20 characters, please enter valid username." )
            username = input('Enter the username to generate the password : ')
        password = RPG()

        while (True):
            print(f'The final {username = } and {password = }')
            chk = input("If you would like to save, press 'Y' or 'y' else 'N' or 'n' : ")
            if chk.lower() == 'y':
                op = open('Users-Pwds.txt','a+')
                op.write(username + ',' + password+'\n')
                op.close()
                break
            elif chk.lower() == 'n':
                chk1 = input("If you would like to generate a new password, press 'Y' or 'y' else 'N' or 'n' : ")
                if chk1.lower() == 'y':
                    password = RPG()
                else:
                    break
        main()

    elif inp == 3:
        ETP()

    else:
        print('Choosen incorrect option. Please try again...')
        main()

if __name__ == '__main__':
    print('------Password Checker------')
    main()
