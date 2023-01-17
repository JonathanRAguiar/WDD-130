def menu():
    play_continue=1
    while play_continue:
        play_continue = int(input("0. Exit \n"+
                              "1. Play \n"))
        if play_continue:
            game()
        else:
            print("Exiting...")

def game():
    check=0

    while win() == 0:
        print("\nPlayer ", check%2 + 1)
        exibe()
        line  = int(input("\nLine :"))
        column = int(input("Column:"))

        if board[line-1][column-1] == 0:
            if(check%2+1)==1:
                board[line-1][column-1]=1
            else:
                board[line-1][column-1]=-1
        else:
            print("Sorry, this space has already been filled")
            check -=1

        if ganhou():
            print("Jogador ",check%2 + 1," ganhou apos ", check+1," rodadas")

        check +=1
    
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1

     #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()
                

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

menu()