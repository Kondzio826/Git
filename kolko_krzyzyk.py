p=["_","_","_","_","_","_"," "," "," "]
i=1
game_end = 0
player1 = "x"
player2 = "o"

def instruction():
    print("Instrukcja pól: \n[1][2][3]\n[4][5][6]\n[7][8][9]\n")

def win():
    game_stat()
    print(f"**** KONIEC GRY, WYGRYWA {player}")
    global game_end
    game_end =1

def game_stat():
    print(f"Plansza gry: \n {p[0]}|{p[1]}|{p[2]}\n {p[3]}|{p[4]}|{p[5]}\n {p[6]}|{p[7]}|{p[8]}")
    print(f"\nRuch: {player}") 

def player_choice():
    choice = 0
    verify = 0
    while choice >9 or choice<1:
        while verify == 0:
            choice = int(input("Jakie pole wybrać(podaj cyfrę)? \n"))
            if p[choice-1] != "x":
                if p[choice-1] != "o":
                    verify = 1
                else:
                    print("POLE ZAJĘTE!!\n")
                    game_stat()
            else:
                print("POLE ZAJĘTE!!\n")
                game_stat()
    verify = 0
    p[choice-1] = player
            
def win_check():
    if p[0] == "x" and p[1] == "x" and p[2] == "X":
        win()
    elif p[3] == "x" and p[4]=="x" and p[5] == "x":
        win()
    elif p[6] == "x" and p[7] == "x" and p[8] == "x":
        win()
    elif p[0] == "x" and p[3] == "x" and p[6] == "x":
        win()
    elif p[1] == "x" and p[4] == "x" and p[7]== "x":
        win()
    elif p[2] == "x" and p[5] == "x" and p[8] == "x":
        win()
    elif p[0] =="x" and p[4] == "x" and p[8]== "x":
        win()
    elif p[2] =="x" and p[4] == "x" and p[6]== "x":
        win()
    elif p[0] == "o" and p[1] == "o" and p[2] == "o":
        win()
    elif p[3] == "o" and p[4]=="o" and p[5] == "o":
        win()
    elif p[6] == "o" and p[7] == "o" and p[8] == "o":
        win()
    elif p[0] == "o" and p[3] == "o" and p[6] == "o":
        win()
    elif p[1] == "o" and p[4] == "o" and p[7]== "o":
        win()
    elif p[2] == "o" and p[5] == "o" and p[8] == "o":
        win()
    elif p[0] =="o" and p[4] == "o" and p[8]== "o":
        win()
    elif p[2] =="o" and p[4] == "o" and p[6]== "o":
        win()

while game_end != 1:
    if i%2 == 0:
        player = player1
    else:
        player = player2

    instruction()
    game_stat()
    player_choice()
    win_check()
    i+=1
    
   


    
