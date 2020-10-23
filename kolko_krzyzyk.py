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

def wincheck():
    triple_win = [[p[0],p[1],p[2]],[p[3],p[4],p[5]],[p[6],p[7],p[8]],[p[0],p[3],p[6]],[p[1],p[5],p[7]],[p[2],p[5],p[8]],[p[0],p[4],p[8]],[p[2],p[4],p[6]]]
    for possibilites in triple_win:
        if possibilites[0] == "x" and possibilites[1] == "x" and possibilites[2] == "x":
            win()
        elif possibilites[0] == "o" and possibilites[1] == "o" and possibilites[2] == "o":
            win()
        else:
            pass

while game_end != 1:
    if i%2 == 0:
        player = player1
    else:
        player = player2

    instruction()
    game_stat()
    player_choice()
    wincheck()
    i+=1