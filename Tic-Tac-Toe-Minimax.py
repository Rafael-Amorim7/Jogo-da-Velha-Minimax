def PrintBoard(board):
    print("Tabuleiro: \n\n")
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):    
            print("X ",end=" ")
    print("\n\n")

def UserTurn(board):
    while True:
        pos=input("Escolha a posição de [1...9]: ")
        pos=int(pos)
        if(board[pos-1]!=0):
            print("\nPosição invalida!")
        else:
            board[pos-1]=-1
            return

def CompTurn(board):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board, -1)
            board[i]=0
            if(score>value):
                value=score
                pos=i
 
    board[pos]=1

def minimax(board,player):
    x=analyzeboard(board)
    if(x!=0):
        return (x*player)
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minimax(board,(player*-1))
            if(score>value):
                value=score
                pos=i
            board[i]=0

    if(pos==-1):
        return 0
    return value
    
def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

def main():
    board=[0,0,0,0,0,0,0,0,0]
    print("\n\nComputador : O Vs. Voce : X")
    player= input("Gostaria de jogar 1º ou 2º: ")
    player = int(player)
    for i in range (0,9):
        if(analyzeboard(board)!=0):
            break
        if((i+player)%2==0):
            CompTurn(board)
        else:
            UserTurn(board)
        PrintBoard(board)
         

    x=analyzeboard(board)
    if(x==0):
         PrintBoard(board)
         print("\nEmpate!!!")
    if(x==-1):
         PrintBoard(board)
         print("\nX Ganhou!!! O Perdeu !!!")
    if(x==1):
         PrintBoard(board)
         print("\nX Perdeu!! O Ganhou !!!!")
       
while True:
    main()