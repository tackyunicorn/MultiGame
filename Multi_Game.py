import pickle
import random
import smtplib
import email.message
import os

def TTT():
    board = {7 : ' ' , 8 : ' ' , 9 : ' ' ,
             4 : ' ' , 5 : ' ' , 6 : ' ' ,
             1 : ' ' , 2 : ' ' , 3 : ' '}

    wins = [[7, 4, 1], [8, 5, 2], [9, 6, 3],  # Vertical
            [7, 8, 9], [4, 5, 6], [1, 2, 3],  # Horizontal
            [7, 5, 3], [1, 5, 9]]             # Diagonal

    def show():
        print board[7] , '|' , board[8] , '|' , board[9]
        print '---------'
        print board[4] , '|' , board[5] , '|' , board[6]
        print '---------'
        print board[1] , '|' , board[2] , '|' , board[3]

    def checkline(char,spot1,spot2,spot3):
        if board[spot1] == char and board[spot2] == char and board[spot3] == char:
            return char

    def checkall(char):
        for x in range(len(wins)):
            if checkline(char, wins[x][0], wins[x][1], wins[x][2]) == char:
                return True

    def oppsel():
        while True:
            random.seed()
            opponent = random.randint(1 , 9)
            if board[opponent] != 'O' and board[opponent] != 'X':
                board[opponent] = 'O'
                break

    def game():
        taken = 0
        result = ''
        while True:

            if checkall('O'):
                result = 'L'
                break

            if taken > 7:
                result = 'T'
                break

            point = input("Choose a spot: ")

            if board[point] != 'X' and board[point] != 'O':
                board[point] = 'X'
                taken += 1
                if checkall('X'):
                    result = 'W'
                    break
            else:
                print("This spot is taken!")
                continue

            oppsel()
            taken += 1

            show()

        return result

    show()
    res = game()
    if res == 'W':
        return 0
    elif res == 'L':
        return 1
    else:
        return 2

def RPS():
    rps = {"rock" : 0 , "paper" : 1 , "scissors" : 2}
    name = ""
    comp_move = ""

    while True:
        name = (raw_input("TYPE Rock,Paper or Scissors: ")).lower()
        if not rps.has_key(name):
            print "Invalid move!"
        else:
            break

    random.seed()
    comp_number = random.randint(0 , 2)
    player_number = rps[name]
    for c in rps.keys():
        if rps[c] == comp_number:
            comp_move = c

    print "The Computer chose: " , comp_move.upper()
    print "You chose: " , name.upper()

    if (comp_number - player_number) % 3 == 0:
        return 2
    elif (comp_number - player_number) % 3 == 1:
        return 1
    else:
        return 0

def GTN():
    count = 0
    for c in range (6):
        random.seed()
        r = random.randint (1 , 10)
        o = random.randint (r , r + 2)
        x = 0

        while True:
            print "Guess a number from " , r , "to " , r + 2 , ": "
            x = input ()
            if x not in range (r , r + 3):
                print "Invalid number"
            else:
                break

        print "The original number is: " , o

        if x == o:
            print "You guessed correctly!"
            count += 1

    if (count == 0):
        print "You haven't guessed any number correctly"
    elif (count == 1):
        print "You have guessed correctly only once"
    else:
        print "You have guessed correctly " , count , "times"

    if count > 3:
        return 0
    elif count < 3:
        return 1
    else:
        return 2

def Mail(ID):
    f = open ("score.p" , 'rb')
    score = pickle.load (f)
    f.close()

    exten = "@gmail.com"

    for c in score.keys():
        if score[ID] > score[c]:
            d = score[ID] - score[c]
            sender = "yourmailserver@gmail.com"
            receiver = c[1] + exten
            message = "Player " + ID[0] + " just beat your score in MultiGame by "\
                      + str(d) + " points!\n" + "Do you have what it takes to beat him?\n" \
                      "Play the game and claim your victory NOW!"

            m = email.message.Message()
            m['From'] = "yourmailserver@gmail.com"
            m['To'] = receiver
            m['Subject'] = "You just got beat!"
            m.set_payload(message)

            try:
                session = smtplib.SMTP('smtp.gmail.com',587)
                session.ehlo()
                session.starttls()
                session.ehlo()
                session.login(sender,'mailserverpassword')
                session.sendmail(sender , receiver , m.as_string())
                session.quit()
                print "Mail sent successfully! "
            except smtplib.SMTPException:
                print('Error...')

def exists():
    try:
        f = open ("score.p" , 'rb')
        f.close()
        return True
    except IOError:
        return False

def win(ID , score):
    score[ID] += 5
    f = open ("score.p" , 'wb')
    pickle.dump (score , f)
    f.close()

def lose(ID , score):
    score[ID] -= 2
    f = open ("score.p" , 'wb')
    pickle.dump (score , f)
    f.close()

def viewscore():
    f = open ("score.p" , 'rb')
    score = pickle.load (f)
    f.close ()
    print "------SCORES------"
    for c in score.keys():
        print c[0] , "\t:\t" , score[c]
    print "------------------"

score = {}
print "Welcome to MultiGame! "
print
name = raw_input("Enter your name: ")
emailID = raw_input("Enter your G-Mail username: ")
print
ID = (name , emailID)

if exists():
    f = open ("score.p" , 'rb')
    score = pickle.load (f)
    f.close()
    if score.has_key(ID):
        print "Welcome back " , ID[0] , " !"
        print
        os.system ('pause')
    else:
        score[ID] = 0
        f = open ("score.p" , 'wb')
        pickle.dump (score , f)
        f.close()
else:
    f = open ("score.p" , 'wb')
    score[ID] = 0
    pickle.dump (score , f)
    f.close()


op = "Y"
while op == "Y":
    os.system ('cls')
    print ("Which game do you want to play? ")
    print ("1. Tic Tac Toe")
    print ("2. Rock Paper Scissors")
    print ("3. Guessing The Number")
    while True:
        option = input ("Enter your option: ")
        if option not in range(1 , 4):
            print "Please enter a number from 1 to 3"
        else:
            if option == 1:
                n1 = TTT()
                if n1 == 0:
                    print "You Win!"
                    win(ID , score)
                elif n1 == 1:
                    print "You Lost..."
                    lose(ID , score)
                else:
                    print "Game ends in a Tie!"
            elif option == 2:
                n2 = RPS()
                if n2 == 0:
                    print "You Win!"
                    win(ID , score)
                elif n2 == 1:
                    print "You Lost..."
                    lose(ID , score)
                else:
                    print "Game ends in a Tie!"
            else:
                n3 = GTN()
                if n3 == 0:
                    print "You Win!"
                    win(ID , score)
                elif n3 == 1:
                    print "You Lost..."
                    lose(ID , score)
                else:
                   print "Game ends in a Tie!" 

            break
    op = (raw_input ("Do you want to play again? (Y/N) ")).upper()

os.system ('cls')
viewscore()
print
Mail(ID)
print
print "Thank you for playing! "
print
os.system('pause')
